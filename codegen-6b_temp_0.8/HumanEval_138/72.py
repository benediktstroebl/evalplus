
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

    # Get the max of 4 even numbers
    n_max = int(n / 2)
    i = 1
    while i <= n_max:
        if is_even(i) and is_even(n - i):
            return True
        i += 2

    return False

