
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n%4!= 0:
        return False
    n_even = n // 2
    if n_even < 4:
        return False
    n_odd = n - n_even
    n_1 = n_even - n_odd
    n_3 = n_odd - n_1
    n_2 = n_odd - n_3
    if n_1 == n_3 == n_2:
        return True
    else:
        return False
