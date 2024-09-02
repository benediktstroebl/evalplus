
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for i in range(10, n//2 + 1):
        for j in range(10, i//2 + 1):
            for k in range(10, j//2 + 1):
                for l in range(10, k//2 + 1):
                    if i + j + k + l == n:
                        return True
    return False
