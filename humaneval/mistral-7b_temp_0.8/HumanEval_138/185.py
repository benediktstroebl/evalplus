
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 4 != 0:
        return False
    for i in range(2, n + 1):
        if i % 2 == 0:
            if i == n:
                return True
            if i in (2, 4, 6):
                if i == n:
                    return True
                if n - i in (2, 4, 6):
                    return True
                if n - i == 8:
                    return True
                if n - i == 10:
                    return True
                if n - i == 12:
                    return True
                if n - i == 14:
                    return True
                if n - i == 16:
                    return True
    return False
