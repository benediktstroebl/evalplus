
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
    # Here are the solutions:
    # 1. Use the function max and -1 as a second argument
    # return max(a, b, -1)
    # 2. Use the function "any" as a second argument
    # return a if a > b else b if a < b else None
    # 3. Use the function "max" as a second argument
    # return max((a, b)) if a > b else (b, a) if a < b else None
    # 4. Use the function "max" and int() as a second argument, which converts
    # float to int
    # return max(int(a), int(b)) if a > b else (b, a) if a < b else None
    # 5. Use the function "any" with 2 arguments
    # return a if a > b else b if a < b else None
    return b if a < b else a if a > b else None
