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
        # If the types are different, return the larger value with its type
        if isinstance(a, int) and isinstance(b, str) and float(b) > a:
            return b
        elif isinstance(b, int) and isinstance(a, str) and float(a) > b:
            return a
        elif isinstance(a, float) and isinstance(b, str) and float(b) > a:
            return b
        elif isinstance(b, float) and isinstance(a, str) and float(a) > b:
            return a
        elif isinstance(a, str) and isinstance(b, int):
            return a
        elif isinstance(a, str) and isinstance(b, float):
            return a
        elif isinstance(b, str) and isinstance(a, int):
            return b
        elif isinstance(b, str) and isinstance(a, float):
            return b
    elif a == b:
        return None
    else:
        return a if a > b else b

# Tests
assert compare_one(1, 2.5) == 2.5
assert compare_one(1, "2,3") == "2,3"
assert compare_one("5,1", "6") == "6"
assert compare_one("1", 1) is None
``` 

This code problem defines a function `compare_one` that accepts two arguments, `a` and `b`, to compare. The function returns the larger value of the two, converted to its original type, or `None` if the two values are equal. The function resists the temptation to convert one of the values to a common type, since the specification states that the function should return the value in its "given variable type." Tests are also included in the code to validate the function. 

This implementation adheres to the requirement that the function returns the larger value in its given type, even if that type is string-based. This is so that strings representing numbers are treated as numbers for the comparison, and are not converted to integers or floats.