```python
def compare_one(a, b):
    """
    Create a function that takes integers, floats, or strings representing
    real numbers, and returns the larger variable in its given variable type.
    Return None if the values are equal.
    Note: If a real number is represented as a string, the floating point might be . or ,
    """
    # check type of a and b, make sure they are the same or convert to float
    if isinstance(a, (int, float)) and isinstance(b, (int, float)):
        if a > b:
            return a
        elif a < b:
            return b
    elif isinstance(a, str) and isinstance(b, str):
        # remove any commas or decimal points
        a = a.replace(",", "")
        b = b.replace(",", "")
        a = a.replace(".", "")
        b = b.replace(".", "")
        # if a and b are both integers, compare them, otherwise compare floats
        if a == b:
            return None
        elif a.isdigit() and b.isdigit():
            return int(a)
        elif a.replace(".", "") == b.replace(".", ""):
            return float(a)
        else:
            return float(a)
    else:
        return None

# Test Suite
def test_compare_one():
    # Test case: Compare two integers
    assert compare_one(1, 2) == 2

    # Test case: Compare two floats
    assert compare_one(2.5, 1.5) == 2.5

    # Test case: Compare two strings representing real numbers
    assert compare_one("2.5", "1.5") == "2.5"

    # Test case: Compare a string and a float
    assert compare_one("3", 3.5) == 3.5

    # Test case: Compare two strings representing the same real number (different delimiters)
    assert compare_one("3.14", "3.14") == "3.14"

    # Test case: Compare two strings representing different real numbers (different delimiters)
    assert compare_one("3.14", "2.78") == "3.14"

    # Test case: Compare two equivalent strings (different delimiters)
    assert compare_one("1,000", "1,000") is None

    # Test case: Compare two unequal strings (different delimiters)
    assert compare_one("1,000", "2,000") == "2,000"

    # Test case: Compare two integers (one is string)
    assert compare_one("2", 2) == 2

    # Test case: Compare two floats (one is string)
    assert compare_one("2.5", 2.5) == "2.5"

    # Test case: Compare two strings (both are strings)
    assert compare_one("2", "3") == "3"

    # Test case: Compare two unequal strings (both are strings)
    assert compare_one("1", "2") == "2"

test_compare_one()
```