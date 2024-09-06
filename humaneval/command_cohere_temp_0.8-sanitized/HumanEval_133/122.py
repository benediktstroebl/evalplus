def sum_squares(lst):
    """
    Return the sum of squared integers in the list, rounding each number to the next bigger integer.
    """
    result = 0
    for n in lst:
        result += int(n + 1e-5) ** 2  # Adding 0.5 * 10^-5 to round each number to the next bigger integer
    return result