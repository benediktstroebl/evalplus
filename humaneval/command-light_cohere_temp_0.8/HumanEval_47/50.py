```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n-1)//2][0] + lst[(n-1)//2][1]) / 2
    else:
        return lst[(n-1)//2][0]

# Test case 1
assert median([3, 1, 2, 4, 5]) == 3

# Test case 2
assert median([-10, 4, 6, 1000, 10, 20]) == 15

# Test case 3
assert median([]) == 0

# Test case 4
assert median([10, 20, 30, 40, 50]) == 50

# Test case 5
try:
    median([-2, -4, -6, -8, -10])
except AssertionError as e:
    print(e)
```