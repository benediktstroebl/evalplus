
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    if n % 4!= 0 or n < 4:
        return False
    else:
        total = n
        for i in range(4):
            total = total - 4
            if total <= 0:
                return True
        return False
