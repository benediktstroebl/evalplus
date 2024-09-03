def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if values are equal.
    """
   
    def comparison(a, b):
        if isinstance(a, (int, float)) and isinstance(b, (int, float)):
            return (a > b)
        elif isinstance(a, str) and isinstance(b, str):
            return str(a) > str(b)
        else:
            return None
    return comparison(a, b)