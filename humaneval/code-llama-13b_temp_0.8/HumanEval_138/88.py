
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    # check if number is even
    if n % 2 == 0:
        sum_odd = 2
        sum_even = 0
        while sum_odd != n:
            sum_odd = sum_odd + 2
            sum_even = sum_even + 2
            if sum_even == n:
                return True
        return False
    else:
        return False
