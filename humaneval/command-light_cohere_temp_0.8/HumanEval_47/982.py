```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[int((n - 1) / 2)]

# Test cases for the median function
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4]) == 3
assert median([10, 20, 30, 1]) == 10
assert median([10, 20, 30, 1, 2]) == 10
assert median([]) == 0
```