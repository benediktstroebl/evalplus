
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    while True:
        if is_number_one_ends(n):
            count += 1
        if n == 0:
            break
        n -=
