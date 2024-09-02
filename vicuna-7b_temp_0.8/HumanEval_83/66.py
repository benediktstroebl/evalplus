
def starts_one_ends(n):
    """
    Given a positive integer n, return the count of the numbers of n-digit
    positive integers that start or end with 1.
    """
    # write your code here
    
    # Example:
    # 5
    # 
    # 1
    # 2 1
    # 3 1 
    # 4 1 2
    # 5 1 2 3
    # 6 1 2 3 4
    # 7 1 2 3 4 5
    # 8 1 2 3 4 5 6
    # 9 1 2 3 4 5 6 7
    # 10 1 2 3 4 5 6 7 8
    # ...
    if n <= 1:
        return 1
    elif n == 2:
        return 1
    else:
        return n // 2
        
