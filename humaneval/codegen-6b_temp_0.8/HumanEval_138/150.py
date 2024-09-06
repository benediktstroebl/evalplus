
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    #check if n can be written as the sum of 4 even numbers
    if n < 4:
        return False
    for i in range(4, n + 1):
        if int(i % 2) == 0 and i + 2 <= n:
            return True
    return False

