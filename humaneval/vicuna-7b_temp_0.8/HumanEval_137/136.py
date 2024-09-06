
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
    if type(a) == type(b):
        if a > b:
            return a
        elif a < b:
            return b
    elif isinstance(a, str) or isinstance(b, str):
        if a.isdigit() and b.isdigit():
            if a.isdecimal() and b.isdecimal():
                if float(a) > float(b):
                    return float(a)
                elif float(b) > float(a):
                    return float(b)
            elif int(a) > int(b):
                return int(a)
            elif int(b) > int(a):
                return int(b)
        elif a != b:
            return b
    return None

comparisons = [compare_one(1, 2.5), compare_one(1, "2,3"), compare_one("5,1", "6"), compare_one("1", 1),
              compare_one("1.5", "1.25"), compare_one("6.5", "6.25"), compare_one(100, 101),
              compare_one(100.1, 101.1), compare_one("100", "101"), compare_one("100.1", "101.1")]

for i in range(len(comparisons)):
    print(f"{comparisons[i] =} {comparisons[i+1]}")