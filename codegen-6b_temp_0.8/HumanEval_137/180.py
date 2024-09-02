
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
    try:
        return int(max(float(a), float(b)))
    except ValueError:
        return None

test_one = compare_one('1', 3)
test_two = compare_one(1, 2.5)
test_three = compare_one('5,1', '6')
