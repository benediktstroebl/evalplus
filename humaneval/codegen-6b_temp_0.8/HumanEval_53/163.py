

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

for x in range(1, 11):
    for y in range(1, 11):
        print(f"{x} + {y} = {add(x, y)}")
