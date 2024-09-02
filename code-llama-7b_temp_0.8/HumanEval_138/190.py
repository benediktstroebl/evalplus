
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Zero is not a positive number
    if n == 0:
        return False

    # One and three are not even numbers
    if n == 1 or n == 3:
        return False

    # Take the first two even numbers
    n_0 = 2
    n_1 = 4

    # And the rest of the even numbers
    n_rest = n - n_0 - n_1
    while n_rest % 2 != 0:
        # Skip all odd numbers
        n_0 = n_1
        n_1 = n_rest
        n_rest = n - n_0 - n_1

    # Check whether the sum is equal to n
    return n_0 + n_1 + n_rest == n

