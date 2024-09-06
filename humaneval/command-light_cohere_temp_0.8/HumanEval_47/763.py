```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]
# Test cases
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4]) == 3
assert median([5, 10, 3, 6, 4]) == 6
assert median([4, 6, 2, 8, 8]) == 4
assert median([1, 2, 3, 4, 5]) != median([3, 1, 2, 4, 5])
assert median([1, 2, 3, 4]) == median([4, 3, 2, 1, 5])
```