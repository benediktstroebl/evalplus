def multiply(a, b):
    """Returns the product of the unit digits of the inputs."""
    return int(str(a)[-1]) * int(str(b)[-1])