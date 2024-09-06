```python
def median(lst):
    """Return the median value of a list of numbers.
    # Sort the acceptable
    first, second, and third pass
    n = len(lst)
    m = n//2
    i = j = 0
    while i < m:
        if lst[i] > lst[j]:
            j = i
        i += 1
    mid = (lst[i] + lst[j]) / 2
    return mid
# Tests
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15
assert median([9, 7, 5, 4, 6]) == 5
assert median([30, 20, 10, 15]) == 15
assert median([9, -9, 7, 5]) == 5
assert median([]) == 0
assert median([1, 2, 3, 4]) == 2
assert median([10, 11, 12]) == 11
```