
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # base case: n=1
    if n==1:
        return 1
    else:
        # recursive case: n>1
        return 1 + starts_one_ends(n-1)
        
