def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type
    if type(a) is not type(b):
        return __compare(a, b)
    # Check value
    if a == b:
        return None
    return __compare(a, b)
def __compare(a, b):
    # Check for string format of real numbers
    if isinstance(a, str) and isinstance(b, str):
        arr = [float(x) for x in a.replace(',', '').replace('.', '').split(' ')]
        brr = [float(x) for x in b.replace(',', '').replace('.', '').split(' ')]
        # Check if first element is larger to avoid bias
        if arr[0] > brr[0]:
            return a
        return b
    # Check integer, float, and string
    if a > b:
        return a
    return b
x = compare_one(1, 2.5)