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
        ("2,5", 2.5, None),
        ("2,5", "2,5", None)
    ]

    if isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        if a.find(",") > -1 and b.find(",") > -1:
            return a if a.strip().is_numeric() > b.strip().is_numeric() else b
        return a if a > b else b
    return None