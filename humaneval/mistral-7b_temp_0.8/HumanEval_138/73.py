
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    is_even = 4 == 0
    i = 0
    while i < 4:
        j = 0
        while j < 4:
            if (i + j + 2) == n:
                if is_even == 0:
                    return True
                else:
                    return False
            elif (i + j + 2) > n:
                j = 4
            elif (i + j + 2) < n:
                j = j + 1
            else:
                j = 4
        i = i + 1
    return False
