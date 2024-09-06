```python
def median(l: list):
    """Return median of elements in the list l.
    assert len(l) >= 2, "Input list must have at least two elements"
    if len(l) % 2 == 0:
        return (l[len(l)//2 - 1] + l[len(l)//2]) / 2
    else:
        return l[len(l)//2]

# Test 1: Check for valid input
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15

# Test 2: Check for odd length
assert median([-10, 4, 6, 1000, 10]) == -10

# Test 3: Check for even length with two identical elements
assert median([-10, -10, -10]) == -10

# Test 4: Check for even length with one identical element
assert median([-20, -10, -10]) == -10

# Test 5: Check for duplicate elements
assert median([-5, -4, -3, -2, -1]) == -2
```