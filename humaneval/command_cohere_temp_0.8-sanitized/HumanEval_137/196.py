def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_true_cases = [
        (1, 2.5, 2.5),
        (1, "2,3", "2,3"),
        ("5,1", "6", "6"),
        ("1", 1, None)
    ]

    compare_false_cases = [
        (2, 3, None),
        (2.5, "2,5", "2,5"),
        ("4", "4", None),
        ("2", 2, None)
    ]

    if type(a) is not type(b):
        if isinstance(a, str) and isinstance(b, str):
            if a.find('.') != -1 and b.find('.') != -1:
                return a if a > b else b
            elif a.find(',') != -1 and b.find(',') != -1:
                return a if a > b else b
            else:
                return a if a > b else b
        elif isinstance(a, float) or isinstance(a, int):
            return a
        else:
            return b
    else:
        return None