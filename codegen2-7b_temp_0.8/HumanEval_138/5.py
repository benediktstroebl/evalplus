
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    return sum(2 * i for i in range(2, int(n / 2) + 1)) == n and sum(2 * i for i in range(1, int(n / 2) + 1)) == n

