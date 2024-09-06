def starts_one_ends(n):
    num = 10**n - 10**(n-1)  # Number of possible numbers without considering starting or ending 1
    num //= 9             # Accounting for the numbers whose last digit is 1 (end with 1)
    num //= 2             # Accounting for the numbers whose first digit is 1 (start with 1)
    return num