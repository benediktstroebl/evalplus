def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # check type of a and b, and convert them to floats for comparison
    if isinstance(a, int) and isinstance(b, int):
        return a if a > b else b
    elif isinstance(a, float) and isinstance(b, float):
        return a if a > b else b
    elif isinstance(a, str) and isinstance(b, str):
        # remove the floating point and compare the strings
        fa, fb = a.strip('.,'), b.strip('.,')
        return fa if fa > fb else fb
    elif isinstance(a, (int, float)) and isinstance(b, str):
        # note: the reverse of previous condition since isinstance is recursive
        fb = b.strip('.,')
        return fb if fb > a else a
    elif isinstance(a, str) and isinstance(b, (int, float)):
        fa = a.strip('.,')
        return fa if fa > b else b
    else:
        return None