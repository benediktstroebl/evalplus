```python
def largest_divisor(n: int) -> int:
    """
    Finds the largest integer that divides the given number evenly, 
    smaller than n.
    """
    def is_multiple_of(x: int, y: int) -> bool:
        return x%y == 0

    if is_multiple_of(y, n):
        return y
    else:
        return n

    return n
 ```