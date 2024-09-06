
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    count = 0
    n_digits = len(str(n))
    for i in range(n):
        if i%10 == 1 and i >= 10**(n_digits-1):
            count += 1
        if (i//10)%10 == 1 and i//10 >= 10**(n_digits-2):
            count += 1
    return count
