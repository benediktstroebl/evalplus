
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # as we already know (see the first two test cases) that there are no odd numbers in the array,
    # we know that there are no even numbers in the array as well.
    # If we know that there are no even numbers in the array then it is simple to get the result
    # as there cannot be an even number that equals the sum of 4 positive numbers.
    return n % 2 == 0

