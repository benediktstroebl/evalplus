```python
def median(lst):
    n = len(lst)
    if n % 2 == 1:
        return (lst[-1] + lst[0]) / 2
    else:
        return lst[int((n-1) / 2)]
# some test cases
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([3, 1, 2, 4, 5]) == 3
assert median([1, 2, 'three']) == 1
assert median([-100, -200, -300]) == 0
assert median([100, 200, 300]) == 200
```