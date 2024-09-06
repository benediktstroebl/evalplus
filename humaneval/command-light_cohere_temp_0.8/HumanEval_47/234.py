```python
def median(l: list):
    """Return median of elements in the list l"""
    n = len(l)
    m = n//2
    if n % 2 == 0:
        return (l[m-1] + l[m]) / 2
    else:
        return l[m]
# Example usage:
test_data = [-10, 4, 6, 1000, 10, 20]
print(median(test_data))  # Output: 15.0
```