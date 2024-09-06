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
    elif type(a) is float and a == b:
        return None
    elif type(a) is str and a == b:
        return None
    elif a > b:
        return a
    else:
        return b
```

The solution uses a conditional statement to compare the variables based on their types, whether they are integers, floats, or strings. Once it determines the larger value, it returns the variable. Or, if the values are equal, it returns `None`. 

You can test this solution by calling the function with different sets of arguments to see if it returns the larger value or none when the values are equal.