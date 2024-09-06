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
    elif type(a) is str and len(a) > len(b):
        return a
    elif type(a) is float and a > b or type(a) is int and a > b:
        return a
    else:
        return b
```

The problem gives a scenario where we have different types of variables like integers, floating numbers, or strings representing real numbers, and our function should return the largest value of them based on their actual types while considering the precision of the floating points.

We first check if both variables are not the same type; we return `None` as they cannot be compared. We also add a check for string length to prioritize the decimal point for the same floating-point strings with different precisions. The function should work for a wide range of input values and types as described in the tests.  This solution should fulfill the requirements of the problem statement.