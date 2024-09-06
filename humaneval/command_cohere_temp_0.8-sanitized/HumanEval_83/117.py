def starts_one_ends(n):
    # Create a list to store the digits
    digits = [0] * n

    # Count the numbers that start with 1
    digits[0] = 1
    for i in range(n):
        if digits[i] != 0:
            digits[i + 1] += digits[i]

    # Return the count of numbers that start or end with 1
    return digits[0] + digits[n - 1]