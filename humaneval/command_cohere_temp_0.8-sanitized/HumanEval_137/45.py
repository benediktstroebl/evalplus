def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) ➞ 2.5
    compare_one(1, "2,3") ➞ "2,3"
    compare_one("5,1", "6") ➞ "6"
    compare_one("1", 1) ➞ None
    """
    if type(a) is not type(b):
        # If the types are different, return the largest priority type
        if isinstance(a, int) and isinstance(b, str):
            return b
        elif isinstance(a, str) and isinstance(b, int):
            return a
        elif isinstance(a, float) and (isinstance(b, int) or isinstance(b, str)):
            return a
        elif isinstance(b, float) and (isinstance(a, int) or isinstance(a, str)):
            return b
        else:
            return None  # Wrong input types, or both strings and equal, return None
    elif a == b:
        return None
    elif isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        # This condition covers string comparison, as well as float-string comparisons
        # with the convention of having . or , as the floating point.
        if a.strip('.,') < b.strip('.,'):
            return a
        else:
            return b