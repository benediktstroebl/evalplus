def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each number to the next bigger integer.
    """
    result = 0
    for n in lst:
        result += int(n + 1e-5) ** 2  # Adding rounding to the next integer
    return result