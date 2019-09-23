
'''In this programm, a password value is set to "Progr@mmer", and the programm ask the user to input the password, if the user input password matches to the saved password , then it displays, "Welcome to the system", otherwise it displays "try again" and if the user enters wrong password 3 times continuously then it displays, "Your account is being blocked for 24hrs and the program ends" '''
def password():
  password="Progr@mmer"
  for count in range(2, -1, -1):
    print("===============================")
    userPwd= input("Enter the password: ")

    if(userPwd==password):
      print("Welcome to the system")
      break

    elif(userPwd!=password and count>0):
      print("Password is wrong, please try again")
      print("Attempts left: ", count )

    if(count==0):
      print("No attempt is left. your account is blocked for 24 hrs")



if __name__=="__main__":
  password()
