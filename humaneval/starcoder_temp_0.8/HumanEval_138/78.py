
def is_equal_to_sum_even(n):
    """Evaluate whether the given number n can be written as the sum of exactly 4 positive even numbers
    Example
    is_equal_to_sum_even(4) == False
    is_equal_to_sum_even(6) == False
    is_equal_to_sum_even(8) == True
    """
    # your code here
    n_lst = list(range(1, n, 2))
    n_lst_sorted = sorted(n_lst)
    if len(n_lst_sorted) > 4:
        return False
    for i in range(0, len(n_lst_sorted) - 3):
        if n_lst_sorted[i] + n_lst_sorted[i + 1] + n_lst_sorted[i + 2] + n_lst_sorted[i + 3] == n:
            return True
    return False
