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

The function compares two numbers, one of which could be a string representing a real number. The function first checks whether the types of the compared variables are the same, then compares the values accordingly. It returns the larger value in its given type or None if the values are equal. 

Here is a simple python file ('problem.py') with a few test cases to test the correctness of the `compare_one` function:
```python
def test_compare_one():
    assert compare_one(1, 2.5) == 2.5
    assert compare_one(1, "2,3") == "2,3"
    assert compare_one("5,1", "6") == "6"
    assert compare_one("1", 1) is None
    assert compare_one(1, 2) is 2
    assert compare_one("3", 3) is None
    assert compare_one(10, "10") == 10
    assert compare_one(11, 11) is None
    assert compare_one("11", 11) == 11
```

You can execute the tests by running `python problem.py` in your terminal to verify the correctness of the solution.