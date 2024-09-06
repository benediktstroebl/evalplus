

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    return x + y

add.short_description = "Addition"
add.description = """Adds two numbers x and y.

Syntax:
add(x, y)

Examples:
add(2, 3) -> 5
add(5, 7) -> 12"""
