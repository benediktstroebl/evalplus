

def string_sequence(n: int) -> str:
    """ Return a string containing space-delimited numbers starting from 0 upto n inclusive.
    >>> string_sequence(0)
    '0'
    >>> string_sequence(5)
    '0 1 2 3 4 5'
    """
    # BASE CASE:
    if n == 0:
        return "0"

    # RECURSIVE CASE:
    elif n > 0:
        return f"{string_sequence(n - 1)} {n}"

    # ERROR CASE:
    else:
        raise ValueError(f"Expected non-negative integer. Got {n}")
