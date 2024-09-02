
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    if n < 0:
        raise ValueError("Number n ({}) must be positive".format(n))
    pos_nums_list = []
    for i in range(0, n // 2 + 1):
        if (i * 2) == n:
            break
        if i * 2 == n:
            pos_nums_list.append(i)
            break
        if i * 2 < n:
            pos_nums_list.append(i)
            if is_equal_to_sum_even(n - i * 2) is True:
                pos_nums_list.append(i)
                break
    if len(pos_nums_list) == 4:
        return True
    return False

