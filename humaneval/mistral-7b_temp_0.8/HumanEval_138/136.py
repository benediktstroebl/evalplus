
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # TODO
    n=int(n)
    if n%2!=0:
        return False
    else:
        x=2
        while(n>x):
            n-=x
            if n==0:
                return True
            elif n==x:
                return False
            x+=2
        return False
