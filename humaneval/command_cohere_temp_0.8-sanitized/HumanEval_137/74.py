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
        # If the types are different, return the larger value WITH its original type
        if isinstance(a, int) and isinstance(b, str) and float(b) > a:
            return b
        elif isinstance(b, int) and isinstance(a, str) and float(a) > b:
            return a
        elif isinstance(a, float) and isinstance(b, int) and a > b:
            return a
        elif isinstance(a, float) and isinstance(b, str) and float(b) > a:
            return b
        elif isinstance(b, float) and isinstance(a, int) and b > a:
            return b
        elif isinstance(b, float) and isinstance(a, str) and float(a) > b:
            return a
        elif isinstance(a, str) and isinstance(b, int) and float(a) > b:
            return a
        elif isinstance(a, str) and isinstance(b, float) and float(b) > a:
            return b
        elif isinstance(a, str) and isinstance(b, str):
            # String values are compared character by character
            # In case of floating point values inside the strings,
            # We consider the point as a digit, so we compare accordingly
            if float(a) > float(b):
                return a
            elif float(b) > float(a):
                return b
        else:
            return None
    elif a == b:
        return None
    else:
        return a