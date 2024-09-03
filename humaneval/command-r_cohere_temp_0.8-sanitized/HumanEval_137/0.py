def compare_one(a, b):
    """
    Compares two variables of type int, float, or str representing real numbers
    and returns the larger one. Returns None if they're equal.
    """
    if type(a) == type(b):
        if isinstance(a, int):
            return max(a, b)
        elif isinstance(a, float):
            return max(a, b)
        elif a.replace(',', '.').replace('.', ',').lower() == b.lower():
            return None
        else:
            return max(a, b)
    else:
        return None