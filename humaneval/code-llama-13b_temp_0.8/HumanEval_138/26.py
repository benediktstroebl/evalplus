
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n == 0:
        return True
    if n < 0 or n % 2 == 1:
        return False
    n /= 2
    for i in range(n - 1):
        for j in range(i, n - 1):
            if i + j + i + j == n:
                return True
    return False

