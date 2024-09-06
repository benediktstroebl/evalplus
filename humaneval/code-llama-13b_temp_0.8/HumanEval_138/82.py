
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n % 2 == 1:
        return False

    if n < 4 or n > 40:
        return False

    if n == 40 and sum([2] * 4) == n:
        return True

    for i in range(2, int(n / 2) + 1):
        if is_equal_to_sum_even(i) and is_equal_to_sum_even(n - i):
            return True
    return False

