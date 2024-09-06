def unique_digits(xs):
    """Return sorted list of elements in xs that contain no even digits."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])