
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

    # If n is odd, check if it can be expressed as the sum of 4 odd numbers
    if n % 2 != 0:
        # Check if n can be expressed as the sum of 4 odd numbers
        if (n // 2) // 2 == 2:
            # If (n // 2) // 2 is 2, n can be expressed as the sum of 4 odd numbers
            return False
        else:
            # If (n // 2) // 2 is not 2, n cannot be expressed as the sum of 4 odd numbers
            return True
    else:
        # Since n is even, it cannot be expressed as the sum of 4 odd numbers
        return True
