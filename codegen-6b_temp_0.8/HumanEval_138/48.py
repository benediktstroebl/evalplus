
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    a, s = n, 0
    while a > 0:
        if a % 2 == 0 and is_even(a):
            if s + a < n:
                s += a
            else:
                return False
        a -= 1
    return s == n
