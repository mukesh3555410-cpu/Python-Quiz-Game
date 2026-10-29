
print("===== ELECTRICITY BILL SYSTEM =====")

units = int(input("Enter electricity units consumed: "))

if units < 0:
    print("Invalid units! Please enter a positive number.")

elif units <= 100:
    bill = units * 1.5

elif units <= 200:
    bill = (100 * 1.5) + ((units - 100) * 2.5)

else:
    bill = (100 * 1.5) + (100 * 2.5) + ((units - 200) * 4)

if units >= 0:
    print("Units consumed:", units)
    print("Electricity bill: Rs.", round(bill, 2))
