
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n_factors = factorization(n)
    count = 0
    for p in n_factors:
        if p % 2 == 0 and p > 0:
            count += 1
    return count == 4

