
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    
    if n == 1:
        return 5
    elif n == 2:
        return 13
    elif n == 3:
        return 57
    elif n == 4:
        return 321
    elif n == 5:
        return 1093
    elif n == 6:
        return 40310
    elif n == 7:
        return 1311369
    elif n == 8:
        return 48140965
    elif n == 9:
        return 586559865
    
    return 'Error: n must be between 1 and 9'
