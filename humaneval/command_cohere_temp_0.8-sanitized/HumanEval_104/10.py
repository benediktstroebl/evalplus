def unique_digits(xs):
    """Return sorted list of elements in xs that contain no even digits."""
    return [x for x in xs if not any(int(d) % 2 == 0 for d in str(x))]