
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # write n as the sum of 4 even numbers
    a, b, c, d = n // 4, n // 4, n // 4, n // 4
    # check if all the numbers are positive
    return all(2**i < n // 4 for i in range(4))
