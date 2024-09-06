def unique_digits(xs):
    """Return sorted list of elements in xs with no even digit."""
    even_digits = [int(d) for d in xs[0]] if len(xs) > 0 else []
    odd_digits = [d for d in xs if d not in even_digits]
    return sorted(odd_digits)