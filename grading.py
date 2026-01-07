print("enter  the marks obtained in all 5 subjects :")
sub1 = int(input("subject 1 :"))
sub2 = int(input("subject 2 :"))
sub3 = int(input("subject 3 :"))
sub4 = int(input("subject 4 :"))
sub5 = int(input("subject 5 :"))
total = sub1 + sub2 + sub3 + sub4 + sub5
avg = total / 5
if avg >= 91 and avg<=100:
    print("Grade A")
elif avg >= 81 and avg<91:
    print("Grade A2")
elif avg >= 71 and avg<81:
    print("Grade B1")   
elif avg >= 61 and avg<71:
    print("Grade B2")
elif avg >= 51 and avg<61:
    print("Grade C1")
elif avg >= 41 and avg<51:
    print("Grade C2")
elif avg >= 33 and avg<41:
    print("Grade D")
else:
    print("Fail")