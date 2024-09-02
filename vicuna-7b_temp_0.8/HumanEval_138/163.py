
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    sum_of_odd_numbers = n - (n // 2)
    if n % 2 == 0:
        return False
    if n % 4 == 0:
        return True
    if n % 2 == 0 and n % 4 == 0:
        return False
    return sum_of_odd_numbers > 0
