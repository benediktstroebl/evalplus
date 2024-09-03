def simplify(x, n):
    """Returns True if x * n evaluates to a whole number, False otherwise.
    Both x and n are in the form <numerator>/<denominator>."""
    x_num, x_denom = map(int, x.split('/'))
    n_num, n_denom = map(int, n.split('/'))
    if x_denom * n_num == x_num * n_denom:
        return True
    return False