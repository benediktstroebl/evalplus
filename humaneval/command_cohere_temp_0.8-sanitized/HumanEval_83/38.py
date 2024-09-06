def starts_one_ends(n):
    # Create a list to store the digits
    digits = list(range(1, n + 1)) * 2
    digits.remove(0)

    # Initialize the count of numbers that start or end with 1
    count = n - 1

    # Consider all permutations of the digits where the first and last digits are fixed
    for i in range(n - 1):
        # Update the count if the current permutation starts and ends with 1
        if digits[i] == 1 and digits[n - 1 - i] == 1:
            count += 1

    return count