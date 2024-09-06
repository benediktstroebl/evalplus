
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    a, b, c, d = 2, 2, 2, 2
    while True:
        if a + b + c + d == n:
            return True
        a += 2
        b += 2
        c += 2
        d += 2
        if a > n or b > n or c > n or d > n:
            return False


