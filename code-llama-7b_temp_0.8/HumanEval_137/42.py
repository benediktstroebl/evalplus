
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
    
    if a == b:
        return None
    
    if type(a) == type(b):
        if isinstance(a, int):
            return max(a,b)
        elif isinstance(a, float):
            return max(a,b)
        elif isinstance(a, str):
            return max(a,b)
    
    if type(a) == int and type(b) == float:
        return max(a,b)
    if type(a) == float and type(b) == int:
        return max(a,b)
    
    if type(a) == int and type(b) == str:
        return max(a,b)
    if type(a) == str and type(b) == int:
        return max(a,b)
    
    if type(a) == float and type(b) == str:
        return max(a,b)
    if type(a) == str and type(b) == float:
        return max(a,b)
    

