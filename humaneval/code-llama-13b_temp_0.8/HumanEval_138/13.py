
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for i in range(1, n // 2):
        for j in range(i + 1, n // 2):
            for k in range(j + 1, n // 2):
                for l in range(k + 1, n // 2 + 1):
                    if i * 2 == j * 2 == k * 2 == l * 2 == n:
                        return True
    return False

