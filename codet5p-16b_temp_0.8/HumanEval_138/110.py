
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    a,b,c,d = 2,2,2,2
    while a < n:
        b = c
        c = d
        if c+d+a+b == n:
            return True
        d = c
    return False
