```python
def median(lst):
    n = len(lst)
    if n <= 1:
        return float('inf')
    m = n//2
    if n % 2 == 0:
        return (lst[m-1] + lst[m]) / 2
    else:
        return lst[m]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([5, 5, 5]) == 5
assert median([10, 20, 10]) == 10
assert median([-100, -80, -60, -40]) == -40

# Another test
lst = [0, 2, 4, 6, 8, 10]
assert median(lst) == 6
```