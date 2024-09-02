
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

    a_type = type(a)
    b_type = type(b)

    if a_type == b_type:

        if a_type == float:
            if b == a:
                return None
            elif b > a:
                return b
            else:
                return a

        if a_type == int:
            if b == a:
                return None
            elif b > a:
                return b
            else:
                return a

        if a_type == str:
            a = float(a.replace(',', '.'))
            b = float(b.replace(',', '.'))
            if a == b:
                return None
            elif b > a:
                return b
            else:
                return a
    else:
        if a_type == float:
            if b_type == int:
                return a
            elif b_type == str:
                b = float(b.replace(',', '.'))
                return a

        if a_type ==
