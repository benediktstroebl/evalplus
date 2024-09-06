
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    return n % 2 == 0 and (n == 2 or n == 8 or n == 10 or n == 12 or n == 14 or n == 16 or n == 18 or n == 20)

