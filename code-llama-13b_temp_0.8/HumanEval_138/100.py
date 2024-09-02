
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n >= 0 and n % 2 == 0:
        odd = n // 2
        for a in range(1, odd + 1):
            if odd >= 2 * a:
                for b in range(a, odd + 1):
                    if odd >= 2 * b:
                        for c in range(b, odd + 1):
                            if odd >= 2 * c:
                                for d in range(c, odd + 1):
                                    if 2 * a + 2 * b + 2 * c + 2 * d == n:
                                        return True
    return False

