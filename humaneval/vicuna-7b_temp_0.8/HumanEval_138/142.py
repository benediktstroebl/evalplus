
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Check if n is odd or even
    if n % 2 != 0:
        return False

    # Check if n can be represented as the sum of 2^i \* 3^j where i and j are non-negative integers
    if (n // 2) % 2 != 0 or (n // 2) // 3 != n // 2:
        return False

    # If n is even and can be represented as the sum of 2^i \* 3^j, it can be written as the sum of 4 positive even numbers
    return True
