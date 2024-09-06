
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # for each of the five positive evens, check whether n-4 is even
    # check even though a negative number is positive
    # return False if n-4 is odd
    return n % 2 == 0 and is_positive_even(n-4)

