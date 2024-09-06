
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    assert n > 0 and n % 2 == 0
    s = 0
    for i in range(2, n, 2):
        if (n - i) % 4!= 0:
            return False
        s += i
    return s == n

