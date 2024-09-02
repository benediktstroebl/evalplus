
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # 0 and 1 are the only single-digit numbers
    # 2-digit numbers = 10 choices for starting with 1 and 10 choices for ending with 1
    # 3-digit numbers = 100 choices for starting with 1 and 100 choices for ending with 1
    # 4-digit numbers = 1000 choices for starting with 1 and 1000 choices for ending with 1
    # 5-digit numbers = 10000 choices for starting with 1 and 10000 choices for ending with 1
    # this is the formula for n-digit numbers
    return sum(10000 if n % 2 == 0 else 100000000 if n > 0 else 0)
