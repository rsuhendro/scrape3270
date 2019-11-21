#
# Sample 3270 screen scraping using py3270 API
#
import time, sys
from py3270 import Emulator

delayt = 1    # In sec, slowing down to be able screen update
mylogin = 'HERC04'
mypass = 'PASS4U'
myhost = '192.168.1.100:3270'
screenrows = []

# use x3270 so you can see what is going on
my3270 = Emulator(visible=True)

# or not (uses s3270)
# my3270 = Emulator()

try:
	# TSO login
	my3270.connect(myhost)
	my3270.wait_for_field()
	#my3270.send_clear()
	my3270.exec_command(b"Clear")
	my3270.wait_for_field()
	time.sleep(delayt)
	if not my3270.string_found(23, 1, 'Logon ===>'):
		sys.exit('Error: print(my3270.string_get(23,1,20))')
	my3270.send_string(mylogin)
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	if not my3270.string_found(1, 2, 'ENTER CURRENT'):
		sys.exit('Error: print(my3270.string_get(1, 2,20))')
	my3270.send_string(mypass)
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	#if not my3270.string_found(13, 2, '***'):
	#    sys.exit('Error: print(my3270.string_get(13,2,10))')
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	#if not my3270.string_found(12, 2, '***'):
	#    sys.exit('Error: print(my3270.string_get(12,2,10))')
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	#if not my3270.string_found(5, 2, 'Option'):
	#    sys.exit('Error: print(my3270.string_get(5,2,10))')
	# 1-RFE
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	# 3-Utilities
	my3270.send_string("3")
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	# 4-DSLIST
	my3270.send_string("4")
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	# DSNAME - HERC03/4
	my3270.send_string(mylogin)
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	# Capture the data set list
	i = 3
	while i < 24:
		if my3270.string_found(i, 4, '**END**'):
			break
		screenrows.append(my3270.string_get(i,4,76))
		i += 1
	#
	my3270.send_pf3()
	my3270.wait_for_field()
	time.sleep(delayt)
	#
	my3270.send_pf3()
	my3270.wait_for_field()
	time.sleep(delayt)
	# 2 - Create Data Set
	my3270.send_string("2")
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	# A - Allocate New Data Set
	my3270.send_string("A")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.send_string("CLIST")
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	# Check if the CLIST data set already exists
	if not my3270.string_found(1, 2, 'Data set already cataloged'):
		my3270.exec_command(b"TAB")
		my3270.send_string("FB")
		my3270.exec_command(b"TAB")
		my3270.send_string("80")
		my3270.exec_command(b"TAB")
		my3270.send_string("1600")
		my3270.exec_command(b"TAB")
		my3270.exec_command(b"TAB")
		my3270.exec_command(b"TAB")
		my3270.send_string("C")
		my3270.exec_command(b"TAB")
		my3270.send_string("1")
		my3270.exec_command(b"TAB")
		my3270.send_string("1")
		my3270.exec_command(b"TAB")
		my3270.send_string("2")
		my3270.send_enter()
		my3270.wait_for_field()
		time.sleep(delayt)
	#
	my3270.send_pf3()
	my3270.wait_for_field()
	time.sleep(delayt)
	#
	my3270.send_pf3()
	my3270.wait_for_field()
	time.sleep(delayt)
	# 2 - Edit 
	my3270.send_string("2")
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	# Clist(hello)
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.send_string("CLIST(HELLO)")
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	# Write down the clist
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.send_string("PROC 0")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.send_string("WRITE HELLO WORLD!")
	my3270.exec_command(b"TAB")
	my3270.exec_command(b"TAB")
	my3270.send_string("Exit")
	my3270.fill_field(2, 15, 'SAVE', 8)
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	#
	my3270.send_pf3()
	my3270.wait_for_field()
	time.sleep(delayt)
	#
	my3270.send_pf3()
	my3270.wait_for_field()
	time.sleep(delayt)
	# TSO command
	my3270.send_string("6")
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	# Exec clist
	my3270.send_string("exec (hello)")
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	#
	my3270.send_pf3()
	my3270.wait_for_field()
	time.sleep(delayt)
	#
	my3270.send_pf3()
	my3270.wait_for_field()
	time.sleep(delayt)
	#if not my3270.string_found(5, 2, 'READY'):
	#    sys.exit('Error: print(my3270.string_get(5,2,10))')
	#
	my3270.send_pf3()
	my3270.wait_for_field()
	time.sleep(delayt)
	#if not my3270.string_found(5, 2, 'READY'):
	#    sys.exit('Error: print(my3270.string_get(5,2,10))')
	#
	my3270.send_string("exec (hello)")
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	#
	my3270.send_string('LOGOFF')
	my3270.send_enter()
	my3270.wait_for_field()
	time.sleep(delayt)
	# disconnect from host and kill subprocess
	my3270.terminate()
	# print out the data set list
	for row in screenrows:
		print(row)

except:
	print ("There was a problem running the script in line: ", sys.exc_traceback.tb_lineno)
	print ("Error: ", sys.exc_info())

