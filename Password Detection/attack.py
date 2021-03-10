import nacl.pwhash
import sys

#save file inputs to variables
hashed = sys.argv[-2]
popular = sys.argv[-1]

#iteration for first file - hashpassword.txt
with open(hashed, "r") as file1:
	for line in file1:
		#save each line without whitespace characters to stripped_line and then save the hashed password to pswd
		stripped_line = line.strip()
		pswd=stripped_line.split()
		#iteration for second file - popularpswd.txt
		with open(popular, "r") as file2:
			for line in file2:
				#save each line without whitespace characters to stripped_line2
				stripped_line2 = line.strip()
				#check if the password from popularpswd.txt is used by a user in hashpassword.txt
				#if it is used, create a new file (results.txt) and save the username and the password
				#if it's not used, print False
				try:
					result = nacl.pwhash.verify(pswd[1].encode("utf-8"), stripped_line2.encode("utf-8"))
					f= open("results.txt","a")
					f.write("%s	%s\n" %(pswd[0],stripped_line2))
					print("That's a match! Found a password!")
				except:
					print("Searching...")
#close files
file1.close()
file2.close()
f.close()
