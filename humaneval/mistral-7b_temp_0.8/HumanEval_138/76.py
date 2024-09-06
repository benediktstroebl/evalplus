
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    # 1
    # n = 8
    # if n % 2 == 0:
    #     n = n // 2
    #     print(n)
    #     return is_equal_to_sum_even(n)
    # else:
    #     return False
    # 2
    if n % 2 == 0:
        return is_equal_to_sum_even(n // 2)
    else:
        return False

