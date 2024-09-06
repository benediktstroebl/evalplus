
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2 == 1:
        return False
    if n <= 0:
        return False
    if n == 2:
        return True
    i = 2
    j = 2
    while i <= n:
        j = 2
        while j < i:
            if i - j == n:
                return True
            j += 2
        i += 2
    return False

