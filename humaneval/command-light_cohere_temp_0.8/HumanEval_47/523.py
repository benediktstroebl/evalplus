```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) >= 2, "Input list must have at least two elements."
    assert all(isinstance(x, numbers. entry([int, float]) for x in l), "Input list must contain numerical elements."
    if len(l) % 2 == 1:
        return l[len(l) // 2]
    else:
        return (l[len(l) // 2 - 1] + l[len(l) // 2]) / 2
```