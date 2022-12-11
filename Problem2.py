Car = {}
brandName = str(input("Enter brand name:"))
Color = str(input("Enter color name:"))
Car = {brandName:Color}
x = open("carDetails.txt","a")
print("brand name and color name:",Car)
print("brand name and color name:",Car,file=x)