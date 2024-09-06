```python
def median(l: list):
    """Return median of elements in the list l"""
    return (sorted(l)[len(l)//2]+sorted((l[len(l)//2]: l[-1])))/2

# Test the function with various test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([]) == 0
assert median([10, 20, 30, 40]) == 10.0
```