#Advanced discount calculation
#A Store Offers Discount Based On Multiple Criteria


premium_member = int(input("Enter Your Premium member Amount :"))

if(premium_member>500):
    print("Congratulations!!!, You Got 20% Discount")
elif(premium_member<500):
    print("Congratulations!!!, You Got 10% Discount")


regular_member = int(input("Enter Your Regular member Amount :"))

if(regular_member>1000):
    print("Congratulations!!!, You Got 15% Discount")
elif(regular_member<=1000 and regular_member>200):
    print("Congratulations!!!, You Got 5% Discount")
elif(regular_member<200):
    print("No Discount Is Applied")
