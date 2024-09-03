```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n-1)//2][0] + lst[n//2][0]) / 2
    else:
        return lst[(n-1)//2][0]

# Test case 1
assert median([3, 1, 2, 4, 5]) == 3

# Test case 2
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test case 3
assert median([1, 2, 3, 4, 5]) == 3

# Test case 4
assert median([10, 10, 10, 10]) == 10

# Test case 5
assert median([10, -10, -20, -20]) == (10 + (-20)) / 2 
```