
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n % 2!= 0:
        return False

    num_2 = n / 2
    num_4 = n / 4

    if num_4 * (num_2 + 1) == n:
        return True

    
