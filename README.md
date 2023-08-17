# HP-Agilent-keysight-6060B-calibration

A simple python script for calibrating an HP/Agilent/Keysight 6060B following the procedure shown in the operating manual

## Introduction

The HP/Agilent/Keysight 6060B is a System DC Electronic load capabale of sinking 300W at 3-60V and 0-60A. It has a constant current, constant voltage and constant resistance modes, supports transient testing with variable frequency, duty cycle and slew rate.

## Disclaimer

A word of caution: Working on or with line voltage and/or high energy equipment can be dangerous and can cause damage, severe injury or death. If you are not authorized or qualified to work on such devices, don’t do it. I don’t take any responsibility for actions you take or the results of these actions. You do everything at your own risk. Be very careful and stay safe. Any information is provided “as is”.

## Calibration/Adjustment

In the readily available service manual HP/Agilent/Keysight specifies a post repair calibration procedure that involves adjusting a trim pot.
Depending on the circumstances it might or might not be a good idea to perform this calibration/adjustment procedure before proceeding with the
"normal" calibration/adjustment procedure that is described in the operating manual. It is strongly recommended to familiarize yourself with the instructions before starting the calibration.

For hobbyists it might be difficult to calibrate the 6060B because of the equipment required. As far as I was able to test, the 6060B performs the calibration steps even if the applied power supply settings deviate slightly from the recommended calibration points, i. e. using a somewhat lower current for the high current range calibration point. This, however, might DEGRADE THE PERFORMANCE of the device.

The provided script follows the procedure shown in the operating manual. It partially automates the process, but changing the setup multiple times during the calibration procedure is to be expected.