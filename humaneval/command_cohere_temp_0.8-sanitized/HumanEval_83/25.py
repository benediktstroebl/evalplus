def starts_one_ends(n):
    # Create a list to store the results for  numbers starting or ending with 1.
    num_start_end_1 = 0

    # Iterate through numbers from 1 to n*10, inclusive.
    for num in range(1, (n * 10) + 1):
        # Count numbers that start with 1 or end with 1.
        if num % 10 == 1:
            num_start_end_1 += 1

    return num_start_end_1