def unique_digits(xs):
    """Return sorted list of elements in xs that have no even digits."""
    result = [x for x in xs if not any(int(y) % 2 == 0 for y in str(x))]
    return sorted(result)