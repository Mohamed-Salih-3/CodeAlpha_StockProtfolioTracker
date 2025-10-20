stock=input("enter stock : ")
quantity=float(input("enter quantity : "))
d={'TCS': 300,
   'VOLVO': 500,
   'NISSAN':350}
a=quantity*d[stock.upper()]
print(a)
with open("file1","w") as f:
    f.write(str(a))



