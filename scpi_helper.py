"""
Provides helper functions to work with scpi enabled instruments via pyvisa
"""


def scpi_bool(scpi_result):
    """
    Converts the string-based scpi boolean representation to a boolean

    :param scpi_result: scpi result representing a boolean
    :result: Boolean value
    """
    try:
        return bool(int(scpi_result))
    except ValueError:
        print(scpi_result)
        raise


def scpi_int(scpi_result):
    """
    Converts the string-based scpi boolean representation to a boolean

    :param scpi_result: scpi result representing a boolean
    :result: Boolean value
    """
    try:
        return int(scpi_result)
    except ValueError:
        return int(float(scpi_result))


def open_scpi_device(resource_manager, res_id, expected_scpi_idn, baud_rate=None, **kwargs):
    """
    Opens the specified resource via visa and checks that the idn string fits
    the expected value

    :param resource_manager: PyVisa resource manager
    :param res_id: Resource identifier string, e. g. 'GPIB0::7::INSTR'
    :param expected_scpi_idn: Excerpt of the SCPI identifier to match against
    :param baud_rate: Baud rate for serial port connections (otherwise optional)
    :param kwargs: Keyword arguments that are passed to the resource manager
    :return: Instrument instance
    """
    inst = resource_manager.open_resource(res_id, **kwargs)
    inst.read_termination = '\n'
    inst.write_termination = '\n'
    if baud_rate is not None:
        inst.baud_rate = int(baud_rate)

    inst_name = inst.query("*IDN?")
    assert expected_scpi_idn in inst_name
    return inst


def setup_scpi_device(inst, timeout=10000, query_delay=0.5):
    """
    Sets up the connection to a scpi device

    :param timeout: How long to wait for a response to a query
    :param query_delay: How long to wait between two queries
    :return: Instrument instance
    """
    inst.write("SYST:REM")                              # Operate the device remotely
    inst.write("*CLS")                                  # Clear any potential error
    inst.timeout = timeout                              # Set a larger response timeout for the scpi device as some measurements might take a while
    inst.query_delay = query_delay                      # Wait a few moments after each query to give the scpi device some processing time

    return inst
