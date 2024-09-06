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
        if a == b:
            compare_val = None
        elif type(a) == str:
            if a.find(',') > -1:
                compare_val = a if a.strip('.') > b.strip('.') else b
            else:
                compare_val = a if a > b else b
        elif type(a) == int:
            compare_val = a if a > b else b
        else:
            compare_val = a if a > b else b
    return compare_val
```

The following test cases illustrate the usage of the `compare_one()` function:
```python
def test_compare_one():
    # Test case one
    assert compare_one(1, 2.5) == 2.5

    # Test case two
    assert compare_one(1, "2,3") == "2,3"

    # Test case three
    assert compare_one("5,1", "6") == "6"

    # Test case four
    assert compare_one("1", 1) is None

test_compare_one()
```

Finally, the tests are executed by calling the `test_compare_one()` function.

You can add more test cases to cover a wide range of scenarios and ensure the correct operation of the `compare_one()` function.