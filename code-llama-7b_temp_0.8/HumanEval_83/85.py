
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Convert the integer into a string
    num_string = str(n)

    # If it doesn't start with 1, we won't count it
    if num_string[0] != '1':
        return 0
    # If it doesn't end with 1, we won't count it
    elif num_string[-1] != '1':
        return 0

    # Otherwise, we'll count it
    else:
        return 1
