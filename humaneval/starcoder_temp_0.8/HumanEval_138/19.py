
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    def is_even(x):
        return (x % 2) == 0

    if n < 0:
        return False

    for i in range(n):
        if is_even(i) and i + (n - i) == n:
            return True
    return False
