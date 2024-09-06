
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
    # Check data type and compare if not same type.
    if (isinstance(a, int) and isinstance(b, float)) or (isinstance(a, float) and isinstance(b, int)):
        if a < b:
            return b
        else:
            return a
    # Check if same type.
    if isinstance(a, float) or isinstance(a, int):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    # Check for strings
    if a[0] == ',' and b[0] == '.':
        a = a.replace(',', '.')
    elif a[0] == '.' and b[0] == ',':
        b = b.replace(',', '.')

    if float(a) > float(b):
        return float(a)
    elif float(a) < float(b):
        return float(b)
    else:
        return None

