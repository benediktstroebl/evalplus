
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is even
    if n % 2 == 0:
        return False
    # Check if n is divisible by 4
    if n % 4 == 0:
        return False
    # Check if n is divisible by 8
    if n % 8 == 0:
        return False
    # Check if n is divisible by 16
    if n % 16 == 0:
        return False
    # If none of the above checks failed, it means that n can be written as the sum of 4 positive even numbers
    return True

