# Scenario 1
# name=input("Enter Your Full Name ")
# tclass=int(input("Enter a number of total classes:"))
# clss=int(input("Enter a number of attendence / classes attanded: (in No(s)):"))
# 
# per=(clss/tclass)*100
# 
# if per  >= 75:
# 	print("You're Allowed to sit in exam ! No Medical")
# elif per>=20 and per<75:
# 	print(f"Dear {name} Your percentage is below 75%")
# 	med_c=int(input("Do you have Medical Certificate?: \Press 1. for Yes \nPress 2. For No \n:"))
# 	if med_c==1:
# 		print("Your Medical certificate is processed for verfication:")
# 		ver=int(input("Let me know is it signed and stimped?: \Press 1. for Yes \nPress 2. For No \n:"))
# 		if ver ==1:
# 			print("Dear {name}, Despit your Attendence is low, but your medical certificate is verified and you're Allowed to sit in exam !")
# 		elif ver ==2:
# 			print("Dear {name},  Your Attendence is low, but your medical certificate is Not verified and you're  Not Allowed to sit in exam !")
# 		else:
# 			print("Invalid input")
# 	else:
# 		print("You're Not Allowed to sit exam!")
# else:
# 	print("Invalid input , Restart the application!")

#Scenario 2

# name=input("Enter your Name:")

# 150-300 60rs per unit for comercial
# 150-300 40rs per unit for residential
# 300-450 85rs per unit for comercial
# 300-450 60rs per unit for residental
# 450-600 100rs per unit for comercial
# 450-600 80rs per unit for residential

name=input("Enter your Name:")
cust_t=int(input("Which customer type are youe? \nPress 1. for Comercial \nPress 2. for residential:\n"))
units=int(input("Number of units you consumed ?:"))
if cust_type==1:
	print(f"Customer Type : Comercial \n Invoice Name : {name}")
	if units>=450 and units<800:
		print(f"Dear {name} \nAs per your {units} \nYou will be charged as Rs 100/Units for comercial \nYour Bill of Electricity for Current Months is \nRs{units*100}")
	elif units>=300 and units<450:
		print(f"Dear {name} \nAs per your {units} \nYou will be charged as Rs 100/Units for comercial \nYour Bill of Electricity for Current Months is \nRs{units*85}")
	elif units>150 and units<300:
		print(f"Dear {name} \nAs per your {units} \nYou will be charged as Rs 100/Units for comercial \nYour Bill of Electricity for Current Months is \nRs{units*65}")
	else:
		print(f"Dear {name} \nAs per your {units} \nYou will be charged as Rs 150/Units for comercial \nYour Bill of Electricity for Current Months is \nRs{units*100}")

