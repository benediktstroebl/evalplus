
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # take the last digit of n
    last_digit = n % 10
    # if it is 1, we need to add 1 to it
    # if it is not 1, we need to take away 1 from it
    if last_digit == 1:
        last_digit = 0
    else:
        last_digit = 10 - last_digit
    # take the first digit of n
    first_digit = n / 10
    # if it is 1, we need to add 1 to it
    # if it is not 1, we need to take away 1 from it
    if first_digit == 1:
        first_digit = 0
    else:
        first_digit = 10 - first_digit
    # the result is the difference between the two digits
    return last_digit - first_digit
