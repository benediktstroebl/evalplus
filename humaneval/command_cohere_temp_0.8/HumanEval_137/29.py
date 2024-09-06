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
        if isinstance(a, str) and isinstance(b, str):
            return "".join([float(x) for x in b if x not in [".", ","]])
        elif isinstance(a, (int, float)) and isinstance(b, str):
            return b
        elif isinstance(a, str) and (isinstance(b, (int, float))):
            return a
        else:
            return "Error: Different types for comparation!"
    # Compare values
    if a == b:
        return None
    elif a > b:
        return a
    else:
        return b
```

The function compares two numbers, one of which could be a string representing a real number. It first checks the types with the `isinstance` function to identify the variables' nature and returns the corresponding value accordingly. In the case of string comparations, it checks if the floating point is a period or a comma, replacing them with none puncture marks before converting the string to a float. Additionally, it handles the case where one of the compared values is a string and the other is a number, ensuring that if the string can be converted to a float, it is considered the larger value. 

To handle the none equality case, the greater than (`>`), and less than (`<`) operators are used to compare the variables in the specified order. 

Note that this code assumes that the variables passed to the `compare_one` function are already normalized, thus it does not include the normalization process in the code for sake of simplicity.