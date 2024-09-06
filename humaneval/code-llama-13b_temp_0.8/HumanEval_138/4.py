
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n % 2 != 0:
        return False

    # Quadratic equation root is √n / 2
    a = 1
    b = -n/2
    c = n

    delta = b**2 - 4*a*c
    if delta == 0:
        return False
    else:
        delta = delta**0.5
        if (delta.is_integer()):
            return True
        else:
            return False
