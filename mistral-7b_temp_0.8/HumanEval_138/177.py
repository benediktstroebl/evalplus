
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    s = 4
    while s <= n:
        if s*2 in range(4, n+1):
            break
        s += 2
    if s*(s+2)*(s+4)/6 == n:
        return True
    return False
