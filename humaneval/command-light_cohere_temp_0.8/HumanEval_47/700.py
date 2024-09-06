```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

#Test cases
assert median([3, 1, 2, 4, 5]) == 3
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([4, 4, 4]) == 4
assert median([1, 2, 3, 4, 5, 6]) == 5
assert median([-1, -2, -3, -4, -5]) == 3
```