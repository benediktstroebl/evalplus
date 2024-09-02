
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is even
    if n % 2 != 0:
        return False

    # Check if n is divisible by 4
    if n % 4 != 0:
        return False

    # Split n into four equal parts
    parts = [n // 4] * 4

    # Check if the sum of the parts is equal to n
    if sum(parts) != n:
        return False

    # Check if all parts are even
    if any(p % 2 != 0 for p in parts):
        return False

    # Return True if all conditions are met
    return True
