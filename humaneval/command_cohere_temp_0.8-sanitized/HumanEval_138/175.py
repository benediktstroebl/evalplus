def is_equal_to_sum_even(n):
    """
    Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    :param n: Number to be evaluated
    :return: True if it can, False otherwise
    """
    if n <= 0:
        return False

    # Try to write n as sum of 4 even numbers
    for i in range(1, int(n**0.5) + 1):
        if n == i * 4:
            return True
        if n == (i * 2) + (i * 2) + (i * 2) + (i * 2):
            return True

    return False