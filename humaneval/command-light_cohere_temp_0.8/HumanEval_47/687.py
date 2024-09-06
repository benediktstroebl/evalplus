```python
def median(l: list):
    """Return median of elements in the list l"""
    return sorted(l)[len(l)//2]
# Example usage:
l = [-10, 4, 6, 1000, 10, 20]
print(median(l))  # Output: 15.0
```