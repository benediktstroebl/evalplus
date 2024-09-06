
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    assert type(n) == int, "n must be an integer"
    assert n >= 4, "n must be greater than or equal to 4"

    even_numbers = [2, 4, 6, 8]
    sum_even_numbers = sum(even_numbers)

    if sum_even_numbers == n:
        return True
    else:
        return False
