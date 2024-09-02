
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    from math import sqrt
    t = int(sqrt(n))
    for i in range(1, t + 1):
        if is_integer(n - i * i):
            a = -(i * i)
            b = (n - i * i) - i
            if is_integer(a) and is_integer(b) and a % 2 == 0 and b % 2 == 0:
                return True
    return False
