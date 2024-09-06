def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    type_a = type(a)
    type_b = type(b)
    
    if type_a == type_b:
        if a == b:
            return None
        elif a > b:
            return a
        else:
            return b
    elif type_a == str and ['', '.', ',', '-.', '1.', '1,', 'e', 'E', 'pi', 'π', 'inf', 'Infinity', '-inf', '-Infinity'].index(a) < ['', '.', ',', '-.', '1.', '1,', 'e', 'E', 'pi', 'π', 'inf', 'Infinity', '-inf', '-Infinity'].index(b):
        return b
    elif type_b == str and ['', '.', ',', '-.', '1.', '1,', 'e', 'E', 'pi', 'π', 'inf', 'Infinity', '-inf', '-Infinity'].index(b) < ['', '.', ',', '-.', '1.', '1,', 'e', 'E', 'pi', 'π', 'inf', 'Infinity', '-inf', '-Infinity'].index(a):
        return a
    elif type_a in [int, float] and type_b in [int, float]:
        return max([a, b])
    else:
        raise ValueError("Enter two comparable values of the same type or transform the values to a common type!")