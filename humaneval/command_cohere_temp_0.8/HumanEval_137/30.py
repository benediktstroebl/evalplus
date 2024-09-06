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
        return max(a, b)
    elif type(a) is float and type(b) is float:
        return max(a, b)
    elif type(a) is str and type(b) is str:
        # Check for precision
        if float(a) == float(b):
            return b
        else:
            return a
    else:
        return None
```

The function `compare_one` in this code takes two arguments and returns the larger value if their types match; otherwise, it returns None. The types that this function can handle are int, float, and string types. This approach ensures that the correct types are being compared while considering the precision of floating-point strings.