def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_result = None
    # Check if a and b are both strings first
    if isinstance(a, str) and isinstance(b, str):
        # Remove spaces and commas, and compare the strings
        compare_result = max(a.replace(',', '').replace(' ', ''), b.replace(',', '').replace(' ', ''))
    # If only one of them is a string, compare using the number representation
    elif isinstance(a, str) or isinstance(b, str):
        # If a is a string, transform a and b to strings
        if isinstance(a, str):
            a = a.replace(',', '').replace(' ', '')
        # If b is a string, transform b and a to strings
        elif isinstance(b, str):
            b = b.replace(',', '').replace(' ', '')
        compare_result = max(a, b)
    # If neither are strings, compare as integers or floats
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        compare_result = max(a, b)
    return compare_result