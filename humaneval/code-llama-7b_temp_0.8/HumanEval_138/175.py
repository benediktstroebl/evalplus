
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if (n % 2 == 1):
        return False
    if (n == 0):
        return False
    else:
        #TODO
        #Determine whether n is even
        #Determine whether n is evenly divisible by 2, 4, 6, 8
        #Do this by subtracting successively by those numbers until n is 0
        #Return whether n is now 0 at the end
        return False




