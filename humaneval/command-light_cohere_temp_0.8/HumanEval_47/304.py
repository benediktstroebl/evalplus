```python
def median(l):
    """Return median of elements in the list l.
    def rounding(x): return int(round(x, 1))
    l = sorted(l)
    m = l[(len(l) + 1) // 2]
    return m if len(l) % 2 != 0 else (m + rounding(l[len(l) - 1])) / 2

# Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15
assert median([-20, -10, -30, 40]) == 20
assert median([1, 2, 3, 4, 5]) == 5
assert median([]) == 0
assert median([10, 20, 30]) == 15
```
This function calculates the median of the list and provides test cases to ensure its correctness.