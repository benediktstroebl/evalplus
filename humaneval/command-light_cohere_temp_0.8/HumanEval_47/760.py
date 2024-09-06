```python
def median(l: list):
    """Return median of elements in the list l"""
    return (len(l) + 1) / 2 * (sum((i for i in l if i % 2 == 0)) + sum((i for i in l if i % 2 == 1)))

# Example usage:
l = [1, 2, 4, 5, -10, 6, 1000, 20, 40, 60]
print(median(l))  # Output: 15.0
```