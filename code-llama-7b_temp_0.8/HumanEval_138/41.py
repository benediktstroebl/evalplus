
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    i = 4
    j = 8
    a = 0
    b = 0
    c = 0
    d = 0
    while j <= n:
        while i <= n:
            if i + j == n:
                return True
            i += 2
        i = 4
        j += 4
    return False

