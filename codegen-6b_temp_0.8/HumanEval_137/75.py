
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
    # write your code below

    def compare_type(x, y):
        """
        If x is an integer & y is a float or a string, return the larger
        variable in its given variable type.

        If x is a float & y is a float, return the larger one of them.
        If x is a string & y is a string, return the largest one of them.
        Otherwise, return None.

        Examples:
        >>> compare_type(1, 2.5)
        2.5
        >>> compare_type(1, "2,3")
        "2,3"
        >>> compare_type("5,1", "6")
        "6"
        >>> compare_type("1", 1)
        1
        >>> compare_type(1, "2")
        2
        >>> compare_type(1, "2.5")
        2.5
        >>> compare_type(2, 1)
        1
        >>> compare_type(2, "1")
        "1"
        """
        if type(x) is int and type(y) is float or type(y) is str:
            if x > y:
                return x
            else:
                return y
        elif type(x) is float and type(y) is float:
            if x > y:
                return x
            else:
                return y
        elif type(x) is str and type(y) is str:
            if x > y:
                return x
            else:
                return y
        else:
            return None

    return compare_type(a, b)

