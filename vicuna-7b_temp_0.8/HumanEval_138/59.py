
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # check if n is even
    if n % 2 == 0:
        return False
    # check if n is less than 16
    if n <= 15:
        # check if n can be expressed as the sum of two positive even numbers
        if n <= 14:
            return True
        # check if n can be expressed as the sum of three positive even numbers
        if n % 3 == 0:
            return True
        # check if n can be expressed as the sum of four positive even numbers
        if n % 4 == 0:
            return True
        # check if n can be expressed as the sum of five positive even numbers
        if n % 5 == 0:
            return True
    return False
