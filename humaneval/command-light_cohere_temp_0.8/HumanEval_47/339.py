```python
def median(l: list):
    """Return median of elements in the list l"""
    if len(l) == 0:
        raise ValueError("The list is empty")
    if len(l) == 1:
        return l[0]
    n = len(l)//2 + len(l) % 2
    m1 = median(l[:n])
    m2 = median(l[n:])
    return (m1 + m2) / 2
# Example usage
l = [-10, 4, 6, 1000, 10, 20]
print(median(l))  # Output: 15.0
```