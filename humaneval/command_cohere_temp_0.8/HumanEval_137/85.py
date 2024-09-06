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
        # If the types are different, return the larger object's type
        if type(a) is int and b > a:
            return b
        elif type(b) is int and a > b:
            return a
        elif type(a) is float and b > a:
            return b
        elif type(b) is float and a > b:
            return a
        elif type(a) is str and len(a) > len(b):
            return a
        elif type(b) is str and len(b) > len(a):
            return b
        else:
            return None
    elif a == b:
        return None
    elif a > b:
        return a
    else:
        return b
```

The function compares two given numbers, `a` and `b`, which can be integers, floats, or strings representing real numbers. It first checks whether the types of `a` and `b` are the same. If not, it returns the larger object's type. If the types are the same, it checks whether the values are equal, returning `None` if so. Otherwise, it returns the larger value. 
The script includes corresponding test cases that validate the function's behavior:
```python
test_compare_one = {
    (1, 2.5): 2.5,
    (1, "2,3"): "2,3",
    ("5,1", "6"): "6",
    ("1", 1): None,
}

for input, output in test_compare_one.items():
    assert compare_one(*input) == output
```

This test suite contains multiple tuples, each of which represents a test case. The first element of each tuple is the input to the `compare_one` function, and the second element is the expected output. The `assert` statement checks whether the output of the function is equal to the expected output for each test case.