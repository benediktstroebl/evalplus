def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This counts the total possible n-digit
    # numbers without considering the starting or ending 1, then subtracts the
    # numbers that have a 1 in non-starting or non-ending positions.
    counts = [n // 2 + n % 2 + 1 for n in range(1, n + 1)]
    for i in range(2, n + 1):
        counts[i] += counts[i - 2]

    # Return the count of valid numbers
    return counts[n] - counts[n - 1]