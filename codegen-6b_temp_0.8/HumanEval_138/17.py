
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n = abs(n)
    for i in range(2,n):
        if n%i!=0:
            continue
        v = n / i
        if v % 2 == 0 and v >= 2:
            return True
    return False
