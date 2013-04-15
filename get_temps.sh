#!/bin/sh

TEMPER_CMD="/usr/bin/temper1"
DEVICE=$1
CONFIG=""
#CONFIG="-C temper1/temper1.conf"
 
if [ "$DEVICE" == "" ]; then
 device_args=""
 cut="2,3"
else
 device_args="-d ${DEVICE}"
 cut="2"
fi

$TEMPER_CMD -u F $CONFIG $device_args | cut -d"," -f $cut

exit 0
