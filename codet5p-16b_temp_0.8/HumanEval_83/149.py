
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    
    starts = 0
    ends = 0
    
    for i in range(10):
        if i == 0:
            starts += 1
        else:
            starts += 10 - i
            
        if i == 0:
            ends += 1
        else:
            ends += i
    
    return starts + ends
