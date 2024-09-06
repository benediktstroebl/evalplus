
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    # You can't write a number as the sum of two even numbers
    if n == 2:
        return False

    # We start the "for loop" at 2, because n cannot be even
    for i in range(2, n):
        # Since a number is even, it's positive
        if i % 2 == 0:
            # The number n can be written as the sum of 2 positive even numbers
            if n == (i + n // i):
                return True

    # The number n cannot be written as the sum of 4 positive even numbers
    return False

