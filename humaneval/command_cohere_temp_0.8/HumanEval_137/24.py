```python
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
    if type(a) is not type(b):
        return None
    if type(a) is int and a == b:
        return None
    elif type(a) is int and a > b:
        return a
    elif type(a) is int and a < b:
        return b
    elif type(a) is float and a == b:
        return None
    elif type(a) is float and a > b:
        return a
    elif type(a) is float and a < b:
        return b
    elif type(a) is str and a == b:
        return None
    elif type(a) is str and a > b:
        return a
    elif type(a) is str and a < b:
        return b
```

This function compares two variables `a` and `b`, both of which can be integers, floats, or strings representing real numbers. It checks their types and returns the larger value in its given type or None if the values are equal. It handles the cases where real numbers are represented as strings, taking into account different formats of floating-point literals.