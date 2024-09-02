
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    n = n // 2 # convert to half
    for a in range(n - 2, 0, -2):
        for b in range(a - 2, 0, -2):
            for c in range(b - 2, 0, -2):
                for d in range(c - 2, 0, -2):
                    if a + b + c + d == n:
                        return True
    return False
