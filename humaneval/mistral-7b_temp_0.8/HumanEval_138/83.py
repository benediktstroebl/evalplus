
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    #TODO - implement this method
    #raise NotImplementedError
    sum=0
    for x in range(0,n+1,2):
        sum+=x
    if sum==n:
        return True
    else:
        return False
    """
    if n%2!=0:
        return False
    sum=0
    for x in range(0,n,2):
        sum+=x
    if sum==n:
        return True
    else:
        return False
    """
