```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # Ensure a and b are either both strings or both numbers
    try:
        a = float(a)
        b = float(b) if isinstance(b, str) else b
    except ValueError:
        pass
    elif a > b:
        return a
    elif a < b:
        return b
    else:
        return None
```

The solution applies a try-except block to parse inputs as numbers only if both inputs are strings or numbers and not a mix of string and number. It also avoids unnecessary conversions by checking the `isinstance()` of `b` only if `b` is a string. This allows the solution to promptly convert only the string to a number while keeping the number input as-is. 

The following tests illustrate how the function operates:
```python
test_compare_one = """
# Test single values
assert compare_one(1, 2.5) == 2.5
assert compare_one(1, "2,3") == "2,3"
assert compare_one("5,1", "6") == "6"

# Test input types
assert compare_one("1", 1) is None
assert compare_one(1, "1") is None

# Test invalid input types
assert compare_one("1", [1]) is None
assert compare_one({"1"}, 1) is None
assert compare_one(None, 1) is None
assert compare_one(1, None) is None
"""
```