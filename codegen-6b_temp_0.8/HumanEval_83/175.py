
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    counter = 0
    for i in range(n):
        temp = i
        while temp > 0:
            if temp % 10 == 1:
                counter += 1
            temp //= 10
    return counter

