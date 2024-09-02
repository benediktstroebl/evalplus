
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    for a in range(0, n - 3):
        for b in range(a + 1, n - 2):
            for c in range(b + 1, n - 1):
                d = n - a - b - c
                if a > b:
                    if c > d:
                        if (a + b + c + d) == n:
                            return True
    return False
