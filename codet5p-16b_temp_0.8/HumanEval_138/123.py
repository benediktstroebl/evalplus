
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    count = 0
    for i in range(4):
        if n % 2 == 0:
            n = n / 2
            count = count + 1
        else:
            break
    if count == 4:
        return True
    return False
