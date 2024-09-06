```python
def median(l):
    """Return median of elements in the list l"""
    if len(l) % 2 == 1:
        return (l[len(l) // 2] + l[len(l) // 2 - 1]) / 2
    else:
        return l[(len(l) - 1) // 2]

# Test case 1
assert median([3, 1, 2, 4, 5]) == 3.0

# Test case 2
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test case 3
assert median([1, 2, 3, 4, 5]) == 3.0

# Test case 4
assert median([10, 20, 30, 40, 30, 40, 30]) == 30.0

# Test case 5
assert median([1000, 2, 3, 1, 4]) == 3.0
```

The median function calculates the median of a given list of numbers and handles different cases: odd numbers, even numbers, and lists with an odd number of elements.