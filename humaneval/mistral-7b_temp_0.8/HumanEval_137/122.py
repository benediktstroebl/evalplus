
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
    #if a==b:
    #    return None
    #elif a>b:
    #    return a
    #elif b>a:
    #    return b
    #a=a.split('.')
    #b=b.split('.')
    #a=float(a[0])+float(a[1])/10**len(a[1])
    #b=float(b[0])+float(b[1])/10**len(b[1])
    #if a==b:
    #    return None
    #elif a>b:
    #    return a
    #elif b>a:
    #    return b
    if a==b:
        return None
    elif isinstance(a, float) and isinstance(b, float):
        return max(a, b)
    elif isinstance(a, int) and isinstance(b, int):
        return max(a, b)
    elif isinstance(a, str) and isinstance(b, str):
        a=float(a.replace(',', '.'))
        b=float
