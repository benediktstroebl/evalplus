def change_base(x: int, base: int):
    """
    Convert a number to a string representation using the specified base.

    Args:
        x: int, the number to be converted
        base: int, the base to use for conversion
    Returns:
        string, the string representation of x using the specified base
    """
    # handle negative numbers by converting to positive and putting base as string before negative
    if x < 0:
        x = abs(x)
        base = str(base) + " " + '-'
    return format(x, '{base}')