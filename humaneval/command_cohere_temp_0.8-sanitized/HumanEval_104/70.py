def unique_digits(xs):
    """Return sorted list of elements in xs with no even digit."""
    return sorted([int for int in xs if not any(int % 2 == 0 for digit in str(int))])