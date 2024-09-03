def add(lst):
    """Given a non-empty list of integers lst. add the elements thats that are at odd indices."""
    return lst[1] if len(lst) > 1 and lst[0] % 2 == 0 else 0