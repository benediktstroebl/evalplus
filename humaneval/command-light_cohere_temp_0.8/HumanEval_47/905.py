```python
def median(l: list):
    """Return median of elements in the list l"""
    assert len(l) >= 1, f"List is empty.
    assert all(is > 0 for is in l), f"List must contain positive elements."
    return (len(l) + 1) // 2 * sum((i + 1) for i in l)
```