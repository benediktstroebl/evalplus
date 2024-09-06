def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_result = None
    if type(a) == type(b) and (type(a) == str or type(a) == int or type(a) == float):
        if a == b:
            compare_result = None
        elif type(a) == str:
            if a.find(',') > -1:
                temp1 = a.rfind(',')
                temp2 = b.rfind(',')
                compare_result = a if temp2 < temp1 else b
            else:
                compare_result = a if a > b else b
        elif type(a) == int:
            compare_result = a if a > b else b
        elif type(a) == float:
            compare_result = a if a > b else b
    return compare_result