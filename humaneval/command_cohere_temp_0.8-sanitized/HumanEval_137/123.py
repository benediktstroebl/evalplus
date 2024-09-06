def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_result = None
    # Check if both inputs are strings, and if the string format is compatible,
    # meaning that they have the same prefix before the first comma or dot.
    if type(a) is str and type(b) is str:
        if ',' in a and ',' in b:
            # Check if the number format is compatible by comparing prefixes
            # before the first comma.
            if a[:a.index(',')] == b[:b.index(',')]:
                compare_result = max(a, b)
        elif '.' in a and '.' in b:
            # Check if the number format is compatible by comparing prefixes
            # before the first dot.
            if a[:a.index('.')] == b[:b.index('.')]:
                compare_result = max(a, b)
    elif type(a) is int and type(b) is int:
        compare_result = max(a, b)
    elif type(a) is float and type(b) is float:
        compare_result = max(a, b)
    elif type(a) is str and type(b) is float:
        compare_result = b
    elif type(a) is float and type(b) is str:
        compare_result = a
    elif type(a) is str and type(b) is int:
        compare_result = a
    elif type(a) is int and type(b) is str:
        compare_result = b
    return compare_result