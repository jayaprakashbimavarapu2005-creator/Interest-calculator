Amount=int(input("enter the amount :"))
Rate=float(input("enter the rate of interest :"))
Time=float(input("enter the time of amount :"))
interest=(Amount*Rate*Time)/100
print("Interest amount",interest)
print("Amount ",Amount)
print("Total Amount ",interest+Amount)