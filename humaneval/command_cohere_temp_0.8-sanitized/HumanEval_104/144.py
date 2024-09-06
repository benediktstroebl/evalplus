def unique_digits(xs):
    """Return sorted list of elements in xs that have no even digits."""
    return sorted([int for int in xs if not any(c in '02468' for c in str(int))])