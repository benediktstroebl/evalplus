
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n%2!=0:
        return False
    a,b,c,d=n//2,n//3,n//4,n//5
    if (a*b*c*d)==n:
        return True
    return False
