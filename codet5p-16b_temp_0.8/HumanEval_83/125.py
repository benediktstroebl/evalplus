
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """

    
    length = len(str(n))
    
    start_one = 0
    end_one = 0
    
    for i in range(1, n+1):
        
        if i < 10:
            start_one += 1
            end_one += 1
        
        elif i >= 10 and i < 100:
            start_one += 2
            end_one += 2
        
        elif i >= 100 and i < 1000:
            start_one += 3
            end_one += 3
        
        elif i >= 1000 and i < 10000:
            start_one += 4
            end_one += 4
        
        elif i >= 10000:
            start_one += 5
            end_one += 5
            
    return start_one + end_one
