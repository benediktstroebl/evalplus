```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (l[n//2 - 1] + l[n//2]) / 2
    else:
        return l[n//2]

# Test case 1: Check if the function correctly calculates the median for a list with an even number of elements
assert(median([3, 1, 2, 4, 5])) == 3.0

# Test case 2: Check if the function correctly calculates the median for a list with an odd number of elements
assert(median([-10, 4, 6, 1000, 10, 20])) == 15.0

# Test case 3: Pass a list with numbers less than 0 and greater than 1000 (Out of range for python list)
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0

# Test case 4: Pass a list containing only one number
assert median([10]) == 10
```