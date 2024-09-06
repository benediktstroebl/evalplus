```python
def median(lst):
    # Sort the list
    lst.sort()
   
    # Find the median by calculating the middle value and dividing by 2
    return (lst[-1] + lst[0]) / 2

# Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3, 4, 5]) == 3.0
assert median([10, 11, 12, 13, 14]) == 13.0
assert median([-100, -150, -200, -250]) == -200
```