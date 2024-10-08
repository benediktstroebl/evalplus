```python
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
    elif type_a == str and type_b != str:
        return a
    elif type_a != str and type_b == str:
        return b
    else:
        return compare_one(str(a), str(b))
```

The solution uses type comparison to check if the types of the variables are the same or if one is a string and then compares the variables accordingly. If the variables are not equal and both are not strings, it recursively calls the function again, this time converting the variables to strings. This way, any real number, including strings, will be properly handled and returned.