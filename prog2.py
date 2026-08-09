amount = int(input("Enter total amount: "))

# Rs. 500 notes
n500 = amount // 500
amount = amount % 500

# Rs. 200 notes
n200 = amount // 200
amount = amount % 200

# Rs. 100 notes
n100 = amount // 100
amount = amount % 100

# Rs. 50 notes
n50 = amount // 50
amount = amount % 50

# Rs. 20 notes
n20 = amount // 20
amount = amount % 20

# Rs. 10 notes
n10 = amount // 10
amount = amount % 10

# Print results
print(f"500 notes : {n500}")
print(f"200 notes : {n200}")
print(f"100 notes : {n100}")
print(f" 50 notes : {n50}")
print(f" 20 notes : {n20}")
print(f" 10 notes : {n10}")
print(f"Remaining : {amount}")