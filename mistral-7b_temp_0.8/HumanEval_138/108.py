
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for x in range(0,n):
        a = n-x
        for y in range(0,a):
            b = a-y
            for z in range(0,b):
                c = b-z
                if x+2*y+2*z+2*c == n:
                    return True
    return False
