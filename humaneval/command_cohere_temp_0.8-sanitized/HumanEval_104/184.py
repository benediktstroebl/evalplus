def unique_digits(xs):
    """Return sorted list of elements in xs that have no even digits."""
    even_digits = [0, 2, 4, 6, 8]
    result = [x for x in xs if not any(d in even_digits for d in str(x))]
    return sorted(result)