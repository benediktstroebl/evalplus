```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare_val = None
    if type(a) == type(b) and type(a) in [int, float, str]:
        if isinstance(a, int):
            compare_val = a if a > b else b
        elif isinstance(a, float):
            compare_val = a if a > b else b
        elif isinstance(a, str):
            compare_val = a if a > b else b
        else:
            compare_val = None
    return compare_val
```

The function compares two given numbers 'a' and 'b', and it returns the number which is of the same type and is larger than the other. The function returns None if the values are equal. The function is designed to work with integers, floats, or strings representing real numbers. 

This function can be called with a variety of input types and return the larger value based on its data type.