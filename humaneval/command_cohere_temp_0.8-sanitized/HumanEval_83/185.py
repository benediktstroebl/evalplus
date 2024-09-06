def starts_one_ends(n):
    # Create a list to store the results for  numbers that start or end with 1.
    ones = [1] * n
    count = 0
    # Calculate the numbers that start with 1
    if ones[0] == 1:
        count += 1
    # Generate the remaining numbers that end with 1
    for i in range(1, n):
        if ones[i] == 1:
            count += 1
    return count