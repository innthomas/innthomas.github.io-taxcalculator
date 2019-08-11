print("PERSONAL INCOME TAX CALCULATOR ")
name = input("Enter your full name:  ")
tin = input("Enter your tax identification number: ")
gi = float(input("Enter your Gross Income: "))
gi_1 = gi*.01
gi_20 = gi*.2
children = int(input("number of children: " ))
children2 = children * 2500
relatives = int(input("number of dependent relatives: " ))
relatives2 = relatives*2000
pension = .075*gi


def first300():
    return 300000*.07

def second300():
    return 300000*.11

def first500():
    return 500000*.15

def second500():
    return 500000*.19

if (gi_1> 200000):
    taxincome = gi_1 + gi_20 + children2 + relatives2 + pension

else:
    taxincome = 200000 + gi_20 + children2 + relatives2 + pension

if (taxincome <= 300000):
    pit = taxincome * .07
elif (taxincome <= 600000):
    pit = first300() + (taxincome *.11)
elif (taxincome <= 1100000):
    pit = second300() + first300() + (taxincome * .15)
elif (taxincome <= 1600000):
    pit = first500() + second300() + first300() +(taxincome * .19)
else:
    pit = second500() + first500() + second300() + first300() + (taxincome * .21)


print("Income tax liability for ", name, " with tin:",tin," is  N",pit)
