
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
    list_a = [a, b]
    list_b = list(map(str, list_a))
    if list_a[0] < list_a[1]:
        return list_a[1]
    if list_b[0] < list_b[1]:
        return list_a[1]
    return None

