```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    compare = None
    if type(a) == type(b) and a != b:
        if type(a) == str:
            compare = a if a.find('.') > b.find('.') else b
        elif type(a) == float:
            compare = a if a > b else b
        elif type(a) == int:
            compare = a if a > b else b
    return compare
```

The solution uses a ternary conditional expression to return the larger value depending on the type of the variables. This is achieved through the use of the `type()` function to determine the variable type for both `a` and `b`. The `compare` variable is assigned the larger value accordingly. If the types are different, or if the values are equal, `compare` will remain `None`. The `find()` method is used to check for the position of a decimal point, to ensure that the larger floating point value is correctly identified.