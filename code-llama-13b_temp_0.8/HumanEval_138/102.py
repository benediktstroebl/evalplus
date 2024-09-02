
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if (n%2==1):
        return False
    sum=0
    for i in range(n//2):
        sum+=2*i
        if sum>n:
            break
        if sum==n:
            return True
    return False
