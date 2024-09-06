def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_one.testnum1 = 1
    compare_one.testnum2 = 2.5
    compare_one.teststr1 = '5,1'
    compare_one.teststr2 = '6'
    compare_one.teststr3 = '1'
    compare_one.testval = None

    if isinstance(a, int) and isinstance(b, int):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif isinstance(a, float) and isinstance(b, (int, float)):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif isinstance(a, (int, float)) and isinstance(b, float):
        if a > b:
            return a
        elif a < b:
            return b
        else:
            return None
    elif isinstance(a, str) and isinstance(b, str):
        if a.strip('.,').isdigit() and b.strip('.,').isdigit():
            if len(a) > len(b):
                return a
            elif len(a) < len(b):
                return b
            else:
                return None
        elif a.strip('.,').replace('.', '', 1).replace(',', '', 1).isdigit() and b.strip('.', ',').isdigit():
            if float(a) > float(b):
                return a
            elif float(a) < float(b):
                return b
            else:
                return None
        else:
            if a > b:
                return a
            elif a < b:
                return b
            else:
                return None
    else:
        return None