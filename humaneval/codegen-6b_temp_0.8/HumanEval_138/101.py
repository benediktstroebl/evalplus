
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 4:
        return False
    n = abs(n)
    b = True
    for i in range(n, 0, -2):
        if b and n - i > 0:
            b = n - i in PRIMES
    return b

