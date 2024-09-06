
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = abs(n)
    if n % 2 == 0:
        n = n // 2
    else:
        n = (n // 2) + 1
    return n % 4 == 0
