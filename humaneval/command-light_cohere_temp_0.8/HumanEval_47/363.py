```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) > 1, "Input list must contain at least two elements"
    assert all(isinstance(x, (int, float)) for x in l), "Input list must contain only numbers"
    if len(l) % 2 == 0:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
    else:
        return l[len(l) // 2]
# Example usage
median([-10, 4, 6, 1000, 10, 20])
 ```