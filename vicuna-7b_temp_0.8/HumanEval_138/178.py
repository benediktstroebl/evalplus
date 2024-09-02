
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # If n is 4k, then it can be written as the sum of 4 positive even numbers
    if n % 4 == 0:
        return True
    # If n is not of the form 4k, then it can be written as the sum of 5 positive numbers, which is not possible
    else:
        return n == 5 or n % 5 == 0