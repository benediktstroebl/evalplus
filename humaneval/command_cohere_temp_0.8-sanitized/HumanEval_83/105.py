def starts_one_ends(n):
    # Create a list to store the count of numbers that start or end with 1
    # for each possible n-digit number. This includes starting with 1 and
    # ending with 1, as well as starting with 1 and ending with 11, and etc.
    counts = [0, 0, 1, 1, 2, 2, 3, 3, 4, 4, 5, 5, 6, 6, 7, 7, 8, 8, 9, 9]
    if n <= 10:
        return counts[n-1]
    else:
        # Calculate the combinations that start or end with 1 for n-digit
        # numbers using the combination formula.
        return combinations_count(n)
def combinations_count(n):
    """
    Calculates the count of combinations of n-items from a set of size n,
    where each selection can be repeated any number of times and none of
    the selections are repeated.
    """
    if n <= 1:
        return 1
    return sum(combinations_count(i) for i in range(n))