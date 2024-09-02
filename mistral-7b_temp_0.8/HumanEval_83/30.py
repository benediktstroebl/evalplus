
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    # Store the count
    counter = 0

    # Check for single digit numbers
    if n == 1:
        return 2

    # Check for 2-digit numbers
    elif n == 2:
        return 4

    # Get the amount of digits in the integer
    else:
        digits = len(str(n))

    # Check for each possible digit
    for i in range(10):
        # Create the string with the number of digits
        string = str(i) * digits

        # Check if the string starts or ends with 1
        if string[0] == "1" or string[-1] == "1":
            counter += 1

    return counter
