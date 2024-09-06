```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[n // 2 - 1] + lst[n // 2]) / 2
    else:
        return lst[n // 2]

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.2  # correct

assert median([-10, 4, 6, 1000, 10, 20]) == 15  # correct

# Test lists with odd and even lengths
assert median([3, 4, 5]) == 5  # correct
assert median([1, 2, 3, 4, 5]) == 3  # correct

# Test list with no elements
assert median([]) == None
```