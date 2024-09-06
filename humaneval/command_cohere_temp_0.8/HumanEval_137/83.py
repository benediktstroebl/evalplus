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
        if issubclass(type(a), str) and type(b) in [int, float]:
            return a
        elif issubclass(type(b), str) and type(a) in [int, float]:
            return b
    # Compare values
    if a == b:
        return None
    return a if a > b else b
```

The solution uses type comparison and value comparison to determine the largest variable type and return the larger value. The function returns `None` if the values are equal. 

The tests for this function would look like this:
```python
# Test 1
assert compare_one(1, 2.5) == 2.5

# Test 2
assert compare_one(1, "2,3") == "2,3"

# Test 3
assert compare_one("5,1", "6") == "6"

# Test 4
assert compare_one("1", 1) is None
``` 
This would ensure that the function behaves as expected.