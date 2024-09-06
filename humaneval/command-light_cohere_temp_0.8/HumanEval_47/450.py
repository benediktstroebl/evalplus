```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n-1)//2][0] + lst[n//2][0]) / 2
    else:
        return lst[(n-1)//2][0]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.5
assert median([-10, 4, 6, 1000, 10, 20]) == 15
```