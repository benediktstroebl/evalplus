
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    return sum(1 for number in range(1, 10 ** n)
               if (str(number)[0] == '1' or str(number)[-1] == '1'))
