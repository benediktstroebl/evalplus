
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # Base case: 0 is the sum of no even numbers
    if n == 0:
        return True
    # Base case: if n is negative, we can't write it as the sum of even numbers
    elif n < 0:
        return False
    # If we've reached this point, n is a positive number
    else:
        # Try all possible even numbers that are less than n
        for i in range(2, n, 2):
            if is_equal_to_sum_even(n - i):
                return True
        # If we got here, no possible combinations of even numbers sum to n
        return False
