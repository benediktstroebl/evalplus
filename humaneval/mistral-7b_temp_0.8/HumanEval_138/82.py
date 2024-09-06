
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # your code here
    if n%4 != 0:
        return False
    else:
        for x in range(n/4):
            if (n/4)-x == x+1:
                return True
            else:
                return False
