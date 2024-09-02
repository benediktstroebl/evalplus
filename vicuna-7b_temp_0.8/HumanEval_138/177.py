
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if the input is 4, 6, or 8
    if n == 4 or n == 6 or n == 8:
        return True
    # Otherwise, check if n can be expressed as the sum of 3 positive even numbers
    return sum(int(n // i) for i in range(3, n + 1)) % 2 == 0
