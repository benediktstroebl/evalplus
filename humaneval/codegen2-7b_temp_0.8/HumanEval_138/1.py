
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 4:
        return False
    return n % 2 == 0 and sum([x for x in range(n) if x % 2 == 0 and x >= 0]) == n

