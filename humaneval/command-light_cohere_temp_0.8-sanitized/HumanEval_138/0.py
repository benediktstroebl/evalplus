def is_equal_to_sum_even(n):
    """
    Checks whether the given number can be represented as the sum of exactly 4 positive even numbers.

    Args:
        n: positive integer

    Returns: boolean value, True if n can be represented as the sum of 4 positive even numbers, False otherwise
    """
    return n % 4 == 0