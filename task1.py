import os
import pyttsx3
print("==========Hiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiiii===================");
pyttsx3.speak("hii")
print("!!!!!######  welcome  menu driven program using Python Code  #####!!!!!")
pyttsx3.speak("welcome menu   driven program using Python Code")
while(True):
	pyttsx3.speak("chat with me with ur requirement")
	p=input("chat with me with ur requirement\n")
	

		
	if((("chrome" in p) or ("google" in p))and("version" in p)and  (("dont" not in p ) and ("no" not in p )and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")			
		os.system("google-chrome --version")					# to get google-chrome version
				



	elif((("document" in p) or ("pdf" in p))and("view" in p)and (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p )and ("no" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("evince")							# to open document viewer
		


	elif((("shotwell" in p) or("gallery" in p)or("image" in p)or ("photo" in p))and(("view" in p)or("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):				
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")		
		os.system("shotwell")							#to open shotwell



	elif((("telegram" in p) )and(("view" in p)or ("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and("no" not in p)and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("/opt/telegram/Telegram")						# to open telegram
		



	elif((("disk" in p)  )and(("view" in p)or ("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)or("info" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and("no" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")		
		pyttsx3.speak("please check the screen once")	
		os.system("baobab")								# to open disk info
		



	elif((("insta" in p)) and (("run" in p) or ("execute" in p) or("log" in p)or ("launch" in p) or ("sign" in p)or("view" in p)or ("account" in p)or("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("google-chrome --app www.instagram.com")   					#to open instagram
		

	elif((("icon" in p) or ("size" in p)or("dock" in p)or("bottom" in p)or("side" in p))and (("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p )and ("no" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("gnome-control-center ubuntu")					# to open icon size settings
		


	elif((("ram" in p) or("system" in p) )and(("view" in p)or ("run" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)or("info" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and("no" not in p)and ("doesn't " not in p) and ("not" not in p))):				
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")		
		os.system("gnome-control-center info-overview")					# to open system info
		
	

	elif((("bluetooth" in p) ) and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and ("no" not in p )and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("gnome-control-center bluetooth")						# to open bluetooth
		


	elif((("liber" in p)or("office" in p) or ("micro" in p)or("docs" in p) )and(("word" in p )or ("write" in p)) and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and ("no" not in p )and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("libreoffice --writer")						# to open liberoffice writer
		
	elif((("liber" in p)or("office" in p) or ("micro" in p)or("docs" in p)or("slide" in p)or("powerpoint"in p) )and(("slide" in p)or("impress" in p )or ("powerpoint" in p)) and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and ("no" not in p )and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("libreoffice --impress")					# to open liberoffice impress


	elif((("wifi" in p) ) and("setting" in p)and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p )and ("no" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("gnome-control-center wifi")							#open wifi settings
			



	elif((("wifi" in p) ) and(("on" in p) or("run" in p) or ("turn" in p)or("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p )and ("no" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("wifi on")								# to turn on wifi
		



	elif((("wifi" in p) ) and(("off" in p) or ("run" in p) or ("turn" in p)or("execute" in p) or ("launch" in p) or("view" in p)or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p )and ("no" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")			
		os.system("wifi off")								# to turn off wifi
		


	elif((("screenshot" in p) )and ("setting" in p)and( ("run" in p) or ("capture" in p)or ("grab" in p)or("take" in p)or ("execute" in p) or ("launch" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):	
		pyttsx3.speak("please wait a moment")		
		os.system("gnome-screenshot -i")					# to open screenshot settings

	elif((("screenshot" in p) )and(("area" in p)or("picture" in p )or("window"in p))and( ("run" in p) or ("capture" in p)or ("grab" in p)or("take" in p)or ("execute" in p) or ("launch" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):	
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("select the area you want to capture")
		print("select the area you want to capture")		
		os.system("gnome-screenshot -a")				# to take screenshot of particular area
		


	elif((("screenshot" in p) )and( ("run" in p) or ("capture" in p)or ("grab" in p)or("take" in p)or ("execute" in p) or ("launch" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):	
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("it capture screenshot after 10 seconds open your screen")
		print("it capture screenshot after 10 seconds open ur screen:")		
		os.system("gnome-screenshot -d 10")					# to take screenshot
		



	elif((("keyboard" in p) or ("shortcuts" in p)) and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")			
		os.system("gnome-control-center keyboard")				# to open keyboard shortcuts 
		



	elif((("sudoku" in p) or ("game" in p)) and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p )and ("no" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")		
		os.system("gnome-sudoku")					# to open  sudoku
			



	elif((("network" in p) or ("proxy" in p))and ("settings" in p)  and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("no" not in p )and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("gnome-control-center network")			# to open network settings
		



	elif((("sound" in p) or ("audio" in p)or("speaker" in p)or ("head " in p)or ("ear" in p))and ("settings" in p)  and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("no" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("gnome-control-center sound")			# to open sound settings
			



	elif((("user" in p)or ("password" in p))and ("settings" in p)  and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p )and ("no" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("gnome-control-center user-accounts")			# to open user settings
		



	elif((("language" in p) or ("langage" in p))and ("settings" in p)  and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("no" not in p )and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("gnome-control-center region")			# to open language settings
			



	elif((("printer" in p) )and ("settings" in p)  and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("no" not in p )and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("gnome-control-center printers")			# to open printer settings
			



	elif((("power" in p) or ("battery" in p)or("screen" in p))and (("settings" in p)or ("percent" in p)or ("%" in p))and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("no" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("gnome-control-center power")			# to open power settings
			



	elif((("display" in p) or ("nightmode" in p) or ("nigthmode" in p) or ("orientation" in p) or ("resolution" in p ))and ("setting" in p)  and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("gnome-control-center display")					# to open display settings
		



	elif((("mouse" in p) or ("touchpad" in p) )and ("setting" in p)  and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and ("no" not in p )and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("gnome-control-center mouse")			# open mouse settings
		

	elif((("date" in p) or ("time" in p) or("zone" in p))and (("run" in p) or ("settings" in p)or("execute" in p) or ("launch" in p) or("view" in p)or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and ("no" not in p )and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		os.system("gnome-control-center datetime")				# to open date and time(settings)
		pyttsx3.speak("please check the screen once")	

	elif((("background" in p) or("setting" in p) ) and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and ("no" not in p )and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("gnome-control-center background")				# to open background settings
		
	elif((("playstore" in p) or("appstore" in p) or ("apps"in p)or ("ubuntu software" in p)or ("software" in p )or("all app" in p)) and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and ("no" not in p )and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("gnome-software")				# to open ubuntu software

	elif((("online" in p) or("accounts" in p) ) and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and ("no" not in p )and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("gnome-control-center online-accounts")				# to open online accounts
		

	elif((("bluetooth" in p) ) and (("run" in p) or("on" in p)or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and ("no" not in p )and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("bluetooth on")							# to turn on bluetooth
		



	elif((("bluetooth" in p) ) and (("run" in p) or("off" in p)or ("execute" in p) or ("launch" in p) or("view" in p)or ("open" in p))and  (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and ("no" not in p )and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("bluetooth off")							# to turn off bluetooth
			



	elif((("firefox" in p) or("chrome" in p) or ("google" in p)or("search" in p )or ("browser" in p) )and("incognito" in p) and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("google-chrome --incognito") 				#to open incognito tab in browser or chrome
		



	elif((("python" in p) or ("pyt" in p))and("version" in p)and  (("dont" not in p ) and ("no" not in p )and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):				
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("python --version")					# to get python version
		
			



	elif((("terminal" in p) or ("blackscreen" in p) or ("code" in p)or ("cli" in p) or ("repl" in p)or("REPL" in p)or("interpreter" in p) or ("command" in p)) and ("python" in p)and (("run" in p) or("view" in p)or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("dont" not in p )and ("no" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("enter  python version")
		a=input("enter version:")
		pyttsx3.speak("please check the screen once")
		print("=*=*=*=*=*=*-*-*-*-*****use exit() command to exit from python REPL =*=*=*=*=*=*-*-*-*-*****");
		if("3" in a):
 			os.system("python3")   						# to open python repl in terminal
		else:
			os.system("python2")
			



	elif((("terminal" in p) or ("blackscreen" in p) or ("code" in p)or ("cli" in p) or ("interpreter" in p) or ("command" in p))and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")					# to open terminal
		os.system("gnome-terminal")
		



	elif((("firefox" in p) or("search" in p )or ("browser" in p) ) and (("run" in p) or ("execute" in p) or("view" in p)or ("launch" in p) or ("open" in p)) and (("dont" not in p )and ("no" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("firefox")									# to open firefox
			



	elif((("google" in p)or ("chrome" in p)or ("browser" in p)) and (("search" in p)) and( ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and ("no" not in p )and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		pyttsx3.speak("enter keywords you want to search")
		p=input("search in google:")
		q="google-chrome --app www.google.com/search?q="+ '"'+p+'"'           		# to search in google
		os.system(q)
			



	elif((("calendar" in p)or("cal" in p)or ("calender" in p) )and (("run" in p) or ("execute" in p) or ("launch" in p) or("view" in p)or ("open" in p))and ( ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("gnome-calendar")								# to open calendar
			



	elif((("camera" in p)or ("capture" in p) or ("cheese" in p) )and (("run" in p) or ("execute" in p) or ("launch" in p) or("view" in p)or ("open" in p))and ( ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")						
		os.system("cheese")				# to open camera



	elif((("chrome" in p) or ("google" in p))and (("run" in p) or ("execute" in p) or ("launch" in p) or("view" in p)or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("google-chrome")					#to open google-chrome	



	elif((("virtual" in p) or ("oracle" in p))and (("run" in p) or ("execute" in p) or ("launch" in p) or("view" in p)or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("VirtualBox")								#to open virtual box
			



	elif((("rhythm" in p) or ("rhytm" in p)or ("audio" in p) or("song" in p) or ("music" in p))and (("run" in p) or("view" in p)or ("play" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("dont" not in p )and ("no" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("rhythmbox") 						# to open audioplayer(rhythmbox)
		



	elif((("vlc" in p) or ("audio" in p) or("music" in p) or ("song" in p)or ("player"in p) or ("video" in p ))and (("run" in p) or("view" in p)or ("play" in p) or ("execute" in p) or ("launch" in p) or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("vlc")								# to open audio or video player(vlc)
			



	elif((("web" in p)or ("url" in p)or ("URL" in p))and (("run" in p) or ("play" in p) or ("execute" in p) or ("launch" in p) or("view" in p)or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("no" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		pyttsx3.speak("enter website URL")
		p=input("enter website URL:")
		q="google-chrome --app "+ p					# to open website using url in browser
		os.system(q)
			



	elif((("youtube" in p)) and (("search" in p)) and( ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("no" not in p )and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		pyttsx3.speak("enter keywords you want to search")
		p=input("search in youtube:")
		q="google-chrome --app www.youtube.com/results?search_query="+ '"'+p+'"'            # to search in youtube
		os.system(q)
			

	

	elif((("youtube" in p)) and (("run" in p) or ("execute" in p) or ("log" in p) or ("sign" in p)or ("launch" in p) or("view" in p)or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("google-chrome --app www.youtube.com")    					# to open youtube
		



	elif((("obs" in p)or("screen recorder" in p)or("screenrecorder" in p)) and (("run" in p) or ("execute" in p) or ("log" in p) or ("sign" in p)or ("launch" in p) or("view" in p)or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("obs-studio")    					# to open obs(screen recorder)
		



	elif((("facebook" in p) or ("fb" in p)) and (("run" in p) or("log" in p)or("sign" in p)or ("execute" in p) or("account" in p)or("view" in p)or ("launch" in p) or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("no" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("google-chrome --app www.facebook.com")   					 #to open facebook
			



	elif((("linked" in p)) and (("run" in p) or("log" in p)or ("execute" in p) or("account" in p)or("view" in p)or("sign" in p)or ("launch" in p) or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("no" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		os.system("google-chrome --app www.linkedin.com")   					 #to open linkedin
			

	

	elif((("text" in p) or("txt" in p)or("file" in p)or("notepad" in p)or("edit" in p)or("editor" in p)or ("gedit" in p)or("code"in p)or(" writer" in p) )and ((("create" in p)or("name " in p))or(("run" in p) or ("execute" in p) or ("launch" in p) or("view" in p)or ("open" in p))) and (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("no" not in p )and ("didn't" not in p )and ("stop" not in p)and("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) and ("not" not in p))):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")
		pyttsx3.speak("enter name of the file")
		p=input("enter file name:");
		q="gedit "+p								# to create a file with given filename
		os.system(q)
			
	


	elif((("text" in p) or("txt" in p)or("file" in p)or("notepad" in p)or("editor" in p)or ("gedit" in p)or("code"in p)or(" writer" in p) )and (("run" in p) or ("execute" in p) or ("launch" in p)or("view" in p) or ("open" in p)) and (("dont" not in p ) and ("didnt" not in p )and ("don't" not in p ) and ("didn't" not in p )and ("stop" not in p)and ("donot" not in p)and("didnot"not in p)and("doesnot" not in p)and ("doesn't " not in p) )):
		pyttsx3.speak("please wait a moment")	
		pyttsx3.speak("please check the screen once")	
		os.system("gedit");							# to open text editor or notepad
		

	else:
		print("not supported");
