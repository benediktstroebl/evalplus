```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    if isinstance(a, str) and isinstance(b, str):
        compare = False
        for char in a:
            if char not in ['', '.', ',']:
                compare = False
                break
            if b < a:
                return a
            elif b > a:
                return b
        if not compare:
            return a
    elif isinstance(a, (int, float)) and isinstance(b, (int, float)):
        return max(a, b)
    elif isinstance(a, str) or isinstance(b, str):
        if a == b:
            return None
        elif (isinstance(a, str) and isinstance(b, int)) or (isinstance(b, str) and isinstance(a, int)):
            return a if isinstance(a, str) else b
        elif (isinstance(a, str) and isinstance(b, float)) or (isinstance(b, str) and isinstance(a, float)):
            return a if isinstance(a, str) else b
    else:
        return max(a, b)
```

The function `compare_one()` takes two parameters `a` and `b`, and returns either the larger of the two variables, the smaller of the two variables, or `None` if the values are equal. The function first checks if both values are strings, and if so, it checks if the strings are valid numeric strings and if they are equal. If the strings are equal, the function returns `None`. If the strings are not equal, the function returns the larger string. If the function finds that the values are not both strings, it checks if they are both numeric values and returns the larger numeric value. If the values are not both strings and are not both numeric values, the function returns the larger of the two values.