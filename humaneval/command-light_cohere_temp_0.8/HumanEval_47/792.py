```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[n // 2] + lst[n // 2 - 1]) / 2
    else:
        return lst[(n // 2) - 1]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15
assert median([-2, 5, 4]) == 2
assert median([3, 4, 2, 8, 1]) == 4
assert median([]) == 0
assert median([21, 12, 13]) == 13
```