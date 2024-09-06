```python
def median(l):
    """Return median of elements in the list l."""
    return (len(l) + 1) / 2 * (sum(sorted(l)) + len(l) * min(l))

# Test the function with various cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15
assert median([10, 10, 10]) == 10
assert median([10, 20, 30]) == 15
assert median([1, 2, 3]) == 2
assert median([-100, -200, -300]) == 200
assert median([20, 10, 30]) == 15
```