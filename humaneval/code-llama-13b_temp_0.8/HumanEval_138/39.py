
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 12:
        return False
    counter = 0
    num = n - 12
    while num >= 0:
        if num % 2 == 0:
            counter += 1
            if counter == 4:
                return True
        num -= 2
    return False

