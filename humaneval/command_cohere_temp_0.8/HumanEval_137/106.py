```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Check type
    if type(a) is not type(b):
        return None
    # Check value
    if a == b:
        return None
    # Determine largest value based on type
    if type(a) is int and type(b) is int:
        return a if a > b else b
    elif type(a) is float and type(b) is float:
        return a if a > b else b
    elif type(a) is str and type(b) is str:
        if a.strip('.,') > b.strip('.,'):
            return a
        else:
            return b
    else:
        return "Error!"
```

The function compares two number-like variables of different types, such as integers, floats, or strings. It first checks their types with `type(a) is not type(b)` to determine if they are not the same. If they are not the same, it returns `None` to indicate that the values are not comparable. If the types are the same, it checks the values with `a == b` for equality and returns `None` if they are equal. The function then branches based on the type to determine the larger value, using the `if` and `elif` statements to ensure the correct type handling. For string types, it uses `strip('.,')` to remove trailing decimal points before making the comparison. If the input types are not integers, floats, or strings, it returns an error message. 

Note that the `compare_one` function will return the larger value in its given variable type, or None if the values are equal. Please let me know if you have any questions!