
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    n = abs(n)
    if n == 0:
        return False
    elif n%2 == 0:
        return n == 4 or n == 6 or n == 8 or n == 10
    else:
        return n % 4 == 0
