def unique_digits(xs):
    """
    Returns a sorted list of all elements in xs that contain no even digits.
    """
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])