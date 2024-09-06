

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    if x == 0:
        return y
    else:
        return add(x - 1, y) + x

