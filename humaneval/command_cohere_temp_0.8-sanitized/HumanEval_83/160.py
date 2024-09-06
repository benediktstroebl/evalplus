def starts_one_ends(n):
    # Create a list to store the digits
    digits = [0] * n

    # Count the numbers that start with 1
    digits[0] = 1
    count_start = 1

    # Count the numbers that end with 1
    count_end = 1

    # Calculate the numbers that start or end with 1
    for i in range(1, n):
        digits[i] = digits[i - 1] + count_start
        count_start = digits[i] + count_end

        # Update the count for numbers ending with 1
        count_end = digits[i]

    return digits[n - 1] + count_end