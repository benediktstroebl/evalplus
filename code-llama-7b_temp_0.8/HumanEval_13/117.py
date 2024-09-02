

def greatest_common_divisor(a: int, b: int) -> int:
    """ Return a greatest common divisor of two integers a and b
    >>> greatest_common_divisor(3, 5)
    1
    >>> greatest_common_divisor(25, 15)
    5
    """
    # Your task is to complete greatest common divisor function
    # You can add your import statements here

    # If b == 0, then a is the greatest common divisor
    if b == 0:
        return a

    # We can assert that a >= b
    # This way we can keep the variables inside the loop smaller
    if a < b:
        a, b = b, a

    # From here, we want to find the greatest common divisor
    # For this, we keep on dividing until b becomes 0
    while b != 0:
        temp = a % b
        a = b
        b = temp
    return a

