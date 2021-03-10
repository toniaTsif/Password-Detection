import nacl.pwhash

#create file for storing username-hashed password pairs
f= open("hashpassword.txt","w+")

#iterate for 10 times to fill the file with adequate data
for x in range(0,10):
	username = input("Please write your username.")
	password = input("Please write your password.")
	#hash the password that the user has given
	hashed = nacl.pwhash.str(password.encode("utf-8"))
	#save to file the username-hashed password pair
	f.write("%s	%s\r" %(username, hashed.decode("utf-8")))
	
#close file when done
f.close()
