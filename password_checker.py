import re

password = input("Enter a password: ")

score = 0

print("\nPassword Check")
print("--------------------")

if len(password) >= 12:
    print("✓ Minimum length met")
    score += 1
else:
    print("✗ Password should be at least 12 characters")

if re.search(r"[A-Z]", password):
    print("✓ Contains uppercase letter")
    score += 1
else:
    print("✗ Missing uppercase letter")

if re.search(r"[a-z]", password):
    print("✓ Contains lowercase letter")
    score += 1
else:
    print("✗ Missing lowercase letter")

if re.search(r"[0-9]", password):
    print("✓ Contains number")
    score += 1
else:
    print("✗ Missing number")

if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
    print("✓ Contains special character")
    score += 1
else:
    print("✗ Missing special character")

print("\n--------------------")

if score == 5:
    print("Password Strength: STRONG")
elif score >= 3:
    print("Password Strength: MEDIUM")
else:
    print("Password Strength: WEAK")