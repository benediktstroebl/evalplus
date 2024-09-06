```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n//2 - 1)] + lst[n//2]) / 2
    else:
        return lst[n//2]
# Test case 1
assertEqual(median([3, 1, 2, 4, 5]), 3.0)
# Test case 2
assertEqual(median([-10, 4, 6, 1000, 10, 20]), 15.0)
# Test case 3
assert median([24, -7, 32, -10, 35]) == -10
```