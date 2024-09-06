def starts_one_ends(n):
    # Create a list to store the digits
    digits = [0] * n

    # Count the numbers that start with 1
    digits[0] = 1

    # Count the numbers that end with 1
    for i in range(n):
        digits[i] += 1
    return digits[0] + digits[n-1]