
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
    a, b = str(a), str(b)
    if a == b:
        return None
    if a == b.replace(',', ''):
        return None
    if b == a.replace(',', ''):
        return None
    if b == a.replace('.', ''):
        return None
    if a == b.replace('.', ''):
        return None
    if abs(float(a) - float(b)) < 0.1:
        return None
    if abs(float(b) - float(a)) < 0.1:
        return None
    if abs(float(a) - float(b)) < abs(float(a) - float(b.replace(',', ''))):
        return str(a)
    return str(b)

