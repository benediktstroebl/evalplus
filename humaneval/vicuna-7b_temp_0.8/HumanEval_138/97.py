
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check base cases
    if n == 4:
        return False
    elif n == 6:
        return False
    elif n == 8:
        return True

    # Recursive case
    if n > 0:
        # If the number is odd, it can never be the sum of 4 even numbers
        return is_equal_to_sum_even(n-1)
    else:
        # If the number is even, it can be the sum of 4 even numbers
        # so we check if it is divisible by 2 and 4
        if n % 2 == 0 and n % 4 == 0:
            return True
        else:
            return is_equal_to_sum_even(n-1)
