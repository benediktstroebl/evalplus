def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes starting with 1 and
    # ending with 1, starting with 1 and ending with 11, and so on.
    counts = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    return counts[n - 1]