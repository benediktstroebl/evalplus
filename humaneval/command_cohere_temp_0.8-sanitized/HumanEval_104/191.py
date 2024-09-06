def unique_digits(xs):
    """Return sorted list of elements in xs with no even digits."""
    return sorted(x for x in xs if not any(int(d) % 2 == 0 for d in str(x)))