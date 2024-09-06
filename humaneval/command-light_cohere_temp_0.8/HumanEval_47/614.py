```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n // 2 - 1] + l[n // 2]) / 2
    else:
        return l[n // 2]
# Sample test cases
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15
assert median([10, 20, 8, 12, 14]) == 12
assert median([1, 2, 3, 4]) == 4
assert median([10, -10, 20, -30]) == 10
assert median([]) == 0
assert median([10, 20, 10]) == 10
```