import fileinput
for line in fileinput.input():
#    line = line.replace("* @param void","*")
#    line = line.replace("in/out","in,out")
#    line = line.replace("@}","@} @}")
#    line = line.replace("::Return","Return")
#    line = line.replace(" ucSuccess"," pucSuccess")
#    line = line.replace("@Reset","@name Reset")
#    line = line.replace("@param[in]  protenset0 Value to be written to PROTENSET0.","@param[in]  block_cfg0 \n @param[in]  block_cfg1")
#    line = line.replace("@param[in]  protenset1 Value to be written to PROTENSET1.","@param[in]  block_cfg2 \n @param[in]  block_cfg3")
#    line = line.replace("@ref BLE_CONN_BW_","BLE_CONN_BW_")
#    line = line.replace("/**@defgroup NRF_CLOCK_LF_XTAL_ACCURACY Clock accuracy * @{ */","/**@defgroup NRF_CLOCK_LF_XTAL_ACCURACY Clock accuracy */")
    line = line.replace("Possible lfclk oscillator","Possible LFCLK oscillator")
    line = line.replace("@ref sd_ble_gap_connect()","sd_ble_gap_connect()")
    print(line)
