
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if (n%2 != 0):
        return False
    else:
        half = int(n/2)
        for i in range(1, half):
            for j in range(i+1, half):
                if (i+j+i+j == n):
                    return True
    return False

