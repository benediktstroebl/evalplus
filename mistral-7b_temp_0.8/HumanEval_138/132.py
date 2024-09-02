
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # can write here the logic that you want to use
    # the solution above works for any number of elements
    # if we want to find a solution for a number that is the sum of 4 even numbers
    # the number must be divisible by 4, 6, 8, 12
    # if a number is not divisible by 4,6,8,12, then the number cannot be written as the sum of 4 even numbers
    # if a number is divisible by one of those numbers, then we have to check if it is divisible by the other 3 numbers
    if n % 4 != 0 or n % 6 != 0 or n % 8 != 0 or n % 12 != 0:
        return False
    else:
        return True
