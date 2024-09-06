
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


    # Given the two variables, what is the best way to convert them to the same type?

    # I'm going to use the float() function to convert both of the values
    # into floats.

    # This will convert 1 into 1.0, and "2,3" into 2.3


    # Now that the values are the same type, we can use the comparison operator
    # (>) to compare them and return the larger one.

    # If the values are equal, we'll return None.

    if float(a) > float(b):
        return float(a)
    elif float(a) < float(b):
        return float(b)
    else:
        return None

