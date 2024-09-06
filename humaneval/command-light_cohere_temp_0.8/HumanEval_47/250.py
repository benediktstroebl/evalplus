```python
def median(l: list):
    """Return median of elements in the list l"""
    n = len(l)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test the function with different input
test_list = [10, 20, 3, -10, 4, 6]
print(median(test_list))  # Output: 5.0
```