def starts_one_ends(n):
    # Create a list to store the digits
    digits = [0] * n

    # Count the numbers that start with 1
    start_with_one = 1 if n == 1 else 0
    for i in range(n):
        digits[i] = 1
        start_with_one += starts_one_ends(n-1)

    # Count the numbers that end with 1
    end_with_one = 1 if n == 1 else 0
    for i in range(n-1, 0, -1):
        digits[i] = 1
        end_with_one += starts_one_ends(n-1)

    return start_with_one + end_with_one