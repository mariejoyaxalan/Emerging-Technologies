print("----------------------------------------------")
print("Emerging Technologies - Laboratory Activity 2")
print("----------------------------------------------")
print("")
pre = float(input("Input your prelim grades: "))
mid = float(input("Input your midterm grades: "))
sfin = float(input("Input your semi-final grades: "))
fin = float(input("Input your final grades: "))
avg = (pre + mid + sfin + fin) / 4
print(" ")
print("Your total average is {}" .format (avg))
if avg >= 75:
  print("==PASSED==")
else:
  print("==FAILED==")