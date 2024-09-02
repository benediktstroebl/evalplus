
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
    # Your code here
    # Set the value of return_value to None
    return_value = None

    # If a is bigger than b
    if a > b:
        # Set the value of return_value to a
        return_value = a
    # If b is bigger than a
    elif b > a:
        # Set the value of return_value to b
        return_value = b
    # Return return_value
    return return_value

