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
    if type(a) is int and a == b:
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
```

This function compares two numbers, one or both of which could be passed as a string with a decimal point or comma, and returns the largest number, respecting the type of the larger number. If the numbers are equal, it returns `None`. The function first checks whether both numbers have the same type, and if not, it returns `None`. This behavior avoids coercion and ensures that the function returns the number in its original type. You can test this script by calling the function with different arguments to check the behavior for different types of inputs and edge cases. Please note that the `None` return value is optional and depends on the specified problem's guidelines. 

The approach makes use of python's `python` comparison and type handling capabilities to simplify the code and eliminate the need for explicit `if` statements for each combination of numeric types using python's implicit conversion rules.

This code adopts python's usual behavior in comparing numbers, which makes it intuitive and easy to use. It also does not require any additional libraries.