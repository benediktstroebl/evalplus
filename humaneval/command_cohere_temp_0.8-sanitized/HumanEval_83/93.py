def starts_one_ends(n):
    num = 10**n - 10**(n-1)  # Number of possible numbers without considering starting or ending 1
    num //= 9             # Adjust for the possibility of the number not ending with a 1
    return num + num - 1  # Add count of numbers starting with 1 and subtract the count of numbers ending with 1