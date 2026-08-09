sub1 = float(input("Enter marks for Subject 1: "))
sub2 = float(input("Enter marks for Subject 2: "))
sub3 = float(input("Enter marks for Subject 3: "))

total_obtained = sub1 + sub2 + sub3
total_possible = 300  # 100 marks per subject

percentage = (total_obtained / total_possible) * 100

print(f"Total Obtained: {total_obtained}/{total_possible}")
print(f"Percentage: {percentage:.2f}%")