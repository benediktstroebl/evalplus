def filter_integers(values: List[Any]) -> List[int]:
    """
    Filter given list of any Python values only for integers.
    """
    int_values = [val for val in values if isinstance(val, int)]
    if not int_values:
        return None
    return int_values