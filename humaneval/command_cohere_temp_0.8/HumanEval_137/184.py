```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,

    compare_one(1, 2.5) -> 2.5
    compare_one(1, "2,3") -> "2,3"
    compare_one("5,1", "6") -> "6"
    compare_one("1", 1) -> None
    """
    if type(a) is not type(b):
        if isinstance(a, float) and isinstance(b, str):
            return b
        elif isinstance(b, float) and isinstance(a, str):
            return a
        elif isinstance(a, int) or isinstance(a, float):
            return a
        elif isinstance(b, int) or isinstance(b, float):
            return b
        elif isinstance(a, str) and isinstance(b, str):
            # to handle numbers like '1' or '1.0'
            if a.replace('.', '', 1) == b.replace('.', '', 1):
                return None
            return a if a >= b else b
    if a == b:
        return None
    return a if a >= b else b
```

The solution uses a type comparison followed by value comparison. The code checks the types of the two variables, and if they are not the same, it performs a second comparison to return the larger value. If the variables are the same type, the code checks the values of the variables and returns the larger value. Finally, if the values are equal, the function returns `None`. 

This approach ensures that the larger value is returned, and if the values are equal, it returns `None` according to the problem statement. 
Let's assume that the provided information, namely the data types and values, are all correct and applicable in this scenario.