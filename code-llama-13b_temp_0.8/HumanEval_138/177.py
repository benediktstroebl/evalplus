
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # check input is valid
    if type(n) != int:
        raise TypeError("n should be an integer")
    # if input is odd, it cannot be written as the sum of 4 positive even numbers
    if n % 2 != 0:
        return False
    
    # try to sum the number with the highest even number smaller than the given number
    # if the result is even, then it must be divisible by 4
    high_even = n - 4
    while high_even > 0:
        if (n - high_even) % 2 == 0:
            return True
        high_even -= 2
    return False
