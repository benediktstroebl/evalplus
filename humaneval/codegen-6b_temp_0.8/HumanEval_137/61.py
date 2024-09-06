
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
    if isinstance(a, int) and isinstance(b, int):
        return a if a > b else b
    elif isinstance(a, str) and isinstance(b, str):
        return a if len(a) > len(b) else b
    return (a if isinstance(a, float) else 0) if (b if isinstance(b, float) else 0) > (a if isinstance(a, float) else 0) else (b if isinstance(b, float) else 0)


assert compare_one(1, 2.5) == 2.5
assert compare_one(1, "2,3") == "2,3"
assert compare_one("5,1", "6") == "6"
assert compare_one("1", 1) is None
assert compare_one(1, "1") is None
assert compare_one("1", 1) is None
assert compare_one("1", "1") is None
assert compare_one(1, 1.9) == 1.9
assert compare_one(1.9, 1) == 1.9
assert compare_one(1.9, 1.9) == 1.9
assert compare_one("1", "1.1") == "1.1"
assert compare_one("1.1", "1") == "1.1"
assert compare_one("1.1", "1.1") == "1.1"
assert compare_one("1", "1,1") == "1,1"
assert compare_one("1,1", "1") == "1,1"
assert compare_one("1,1", "1,1") == "1,1"
assert compare_one("1", "1.1,1.1") == "1.1,1.1"
assert compare_one("1.1", "1.1,1.1") == "1.1,1.1"
assert compare_one("1.1,1.1", "1.1,1.1") == "1.1,1.1"
assert compare_one("1.1,1.1", "1.1,1.1") == "1.1,1.1