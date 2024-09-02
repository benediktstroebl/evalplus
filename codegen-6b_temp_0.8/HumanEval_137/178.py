
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
    def bigger(var1, var2):
        if str(var1).lower() == str(var2).lower():
            return None
        if type(var1) == str:
            var1 = float(var1.replace(',', '.'))
        if type(var2) == str:
            var2 = float(var2.replace(',', '.'))
        if var1 > var2:
            return var1
        else:
            return var2

    return bigger(a, b)
