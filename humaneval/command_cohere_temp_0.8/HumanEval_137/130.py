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
    elif type(a) is int and a == b:
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
    else:
        return None
```

The function compares two numbers, one of which could be a string representing a real number. It checks the types of the two objects with the `type` attribute, returning `None` if the types are different. It also returns `None` if the values are equal. If the number is an integer and is larger than the other number, it returns the integer. If the number is a float and is larger than the other number, it returns the float. If the number is a string and is larger than the other number, it returns the string. If the two numbers have different types and are not equal, `None` is returned.