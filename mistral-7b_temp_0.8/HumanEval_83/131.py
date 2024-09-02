
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    #This line gets the length of the number
    num_len = len(str(n))

    #This line gets the total numbers of digits in the number
    num_dig = (10 ** num_len) - 1

    #This line adds one if the number ends with 1
    if n % 10 == 1:
        num_dig += 1

    #This line returns the number of digits in the number
    return num_dig
