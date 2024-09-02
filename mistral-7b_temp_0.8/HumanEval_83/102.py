
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Initialize a counter to keep track of the number of n-digit positive integers that start or end with 1
    counter = 0

    # Check if the number of digits in n is less than 1
    if len(str(n)) < 1:
        return counter

    # Check if the first digit of n is 1
    if str(n)[0] == "1":
        counter += 1

    # Calculate the number of 1s that can be inserted at the beginning of each number
    # from 1 to n-1 (inclusive)
    for i in range(1, n):
        if str(i)[:1] == "1":
            counter += 1

    # Calculate the number of 1s that can be inserted at the end of each number
    # from 1 to n-1 (inclusive)
    for i in range(1, n):
        if str(i)[-1:] == "1":
            counter += 1

    # Return the counter
    return counter

