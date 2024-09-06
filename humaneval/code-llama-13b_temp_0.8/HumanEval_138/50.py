
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # We know that the sum of even numbers is even
    if n % 2 != 0:
        return False

    # It is not possible to be the sum of even numbers if it is not even
    if n < 2:
        return False

    # Start with smallest even number and increment by 2
    # If a number cannot be written as the sum of 4 even numbers, go to the next one
    for i in range(2, n, 2):
        if n - i - i >= 2:
            if (n - i - i) % 2 == 0:
                return True

    # If none of the previous numbers can be written as the sum of 4 even numbers, return false
    return False
