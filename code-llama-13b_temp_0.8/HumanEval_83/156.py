
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # Convert n to a string.
    n_as_string = str(n)

    # Initialize a counter.
    count = 0

    # Iterate over all possible numbers of n-digits.
    for i in range(10 ** (n - 1), 10 ** n):
        # Convert i to a string.
        i_as_string = str(i)

        # Check if i starts with a 1 or ends with a 1.
        if i_as_string[0] == "1" or i_as_string[-1] == "1":
            # Increment the counter.
            count += 1

    return count
