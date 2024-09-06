```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    else:
        return (len(lst) + 1) // 2 * (lst[len(lst) - 1] + lst[len(lst) // 2])

# Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4]) == 2.5
assert median([10, 10, 20, 30]) == 20
```