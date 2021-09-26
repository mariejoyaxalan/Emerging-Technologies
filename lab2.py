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
if avg >= 99 and avg <= 100:
    print("Your total average is {}" .format(avg) + ". \nYour grade is A. \nCongratulations, you PASSED!")
elif avg >= 90 and avg <= 98:
    print("Your total average is {}" .format(avg) + ". \nYour grade is B. \nCongratulations, you PASSED!")
elif avg >= 80 and avg <= 89:
    print("Your total average is {}" .format(avg) + ". \nYour grade is C. \nCongratulations, you PASSED!")
elif avg >= 75 and avg <= 79:
    print("Your total average is {}" .format(avg) + ". \nYour grade is D. \nCongratulations, you PASSED!")
elif avg >= 70 and avg <= 74:
    print("Your total average is {}" .format(avg) + ". \nYour grade is D. \nUnfortunately, you FAILED.")
elif avg >= 61 and avg <= 69:
    print("Your total average is {}" .format(avg) + ". \nYour grade is E. \nUnfortunately, you FAILED.")
elif avg < 60:
    print("Your total average is {}" .format(avg) + ". \nYour grade is F. \nUnfortunately, you FAILED.")
else:
    print("Invalid input!")