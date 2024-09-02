
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # check base cases
    if n <= 4:
        return True
    elif n % 2 == 0:
        return False
    else:
        if n > 2*sum(map(int, str(n // 2))) and n % 4 == 0:
            return True
        else:
            return False
