
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 8:
        return False
    even_number = 2
    for _ in range(4):
        if n - even_number < even_number:
            return False
        even_number += 2
    return True
