def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    type_a = type(a)
    type_b = type(b)
    
    # check if the types are different, use max
    if type_a != type_b:
        if type_a in [int, float] and type_b in [int, float]:
            return max([a, b])
        # if one type is string, return the string
        return max([str(a), str(b)])
    
    # check if the values are equal, return None
    if a == b:
        return None
    
    # check if the values are integers, return the integer
    if type_a == int and type_b == int:
        return max([a, b])
    
    # check if the values are floats, return the float
    if type_a == float and type_b == float:
        return max([a, b])
    
    # here the values are strings, return the string
    return max([a, b])