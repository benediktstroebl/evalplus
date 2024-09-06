
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    factors = prime_factors(n)
    if factors:
        for i in factors:
            if i % 2 == 0 and factors.count(i) != 4:
                return False
    return True
