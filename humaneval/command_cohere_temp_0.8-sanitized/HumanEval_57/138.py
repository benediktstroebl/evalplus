def monotonic(l):
    """Return True if list elements are monotonically increasing or decreasing."""
    try:
        yield l.sort() == l if l else True
    except TypeError:
        return any(el <= prev or el >= next for el, prev, next in zip(l, l[1:], l[2:]))