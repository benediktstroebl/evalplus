
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """

    # [2, 2, 2, 2]
    # [4, 2, 2, 2]
    # [8, 2, 2, 2]
    # [4, 4, 2, 2]
    # [6, 4, 2, 2]
    # [8, 4, 2, 2]

    # 4
    # 2
    # 1
    # 0
    # -1
    # -2
    # -3

    # 16 == 4 + 4 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2
    # 14 == 4 + 4 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2
