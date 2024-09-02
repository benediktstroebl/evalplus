
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n <= 4:
        return False
    elif n % 2 != 0:
        return False
    else:
        for i in range(3, n // 2 + 1, 2):
            for j in range(i + 1, n + 1, 2):
                if (n // (i + 2) - (j // 2)) % 2 != 0:
                    return False
        return True
