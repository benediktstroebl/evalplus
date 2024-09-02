
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for x in range(1,n):
        for y in range(1,n):
            for z in range(1,n):
                for w in range(1,n):
                    if (x+y+z+w) == n and (x*2+y*2+z*2+w*2) == n:
                        return True
    return False


