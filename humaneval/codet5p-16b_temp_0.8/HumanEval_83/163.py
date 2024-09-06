
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    
    count = 0
    
    for i in range(0, n):
        number = str(i)
        if (len(number) == 1) and (number[0] == '1'):
            count += 1
        if (number[0] == '1'):
            count += 1
        if (number[-1] == '1'):
            count += 1
            
    return count
    
    
