
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n%4 != 0:
        return False
    sum_of_numbers = n//4
    while sum_of_numbers >= 4:
        if n%sum_of_numbers == 0:
            break
        sum_of_numbers -= 1
    else:
        return False
    return True
