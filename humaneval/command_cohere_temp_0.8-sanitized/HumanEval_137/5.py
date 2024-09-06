def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_result = None
    # Check if `a` and `b` are of the same type
    if type(a) == type(b):
        if isinstance(a, int) and a >= b:
            compare_result = a
        elif isinstance(a, float) and a > b:
            compare_result = a
        elif isinstance(a, str) and a >= b:
            compare_result = a
        elif a == b:
            compare_result = None
    elif type(a) == str or type(b) == str:
        if isinstance(a, str) and isinstance(b, str):
            if a.strip('.,').isdigit() and b.strip('.,').isdigit():
                compare_result = int(b) if int(a) < int(b) else int(a)
            elif a.strip('.,').replace('.', '').replace(',', '').isdigit() and b.strip('.,').replace('.', '').replace(',', '').isdigit():
                compare_result = float(b) if float(a) < float(b) else float(a)
            elif a >= b:
                compare_result = a
            else:
                compare_result = b
        elif isinstance(a, str):
            compare_result = a
        else:
            compare_result = b
    elif type(a) == int:
        compare_result = a
    elif type(b) == int:
        compare_result = b
    elif type(a) == float:
        compare_result = a
    elif type(b) == float:
        compare_result = b
    return compare_result