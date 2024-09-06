```python
def median(lst):
    """Return median of elements in the list lst"""
    if len(lst) % 2 == 0:
        return (lst[(len(lst) / 2) - 1] + lst[len / 2]) / 2
    else:
        return lst[(len(lst) - 1) ]

#Test cases
assert median([3, 1, 2, 4, 5]) == 3.0
assert median([-10, 4, 6, 1000, 10, 20]) == 15.0
assert median([1, 2, 3]) == 2.0
assert median([5, 5, 4, 4, 3]) == 4.0
assert median([1, 2, 3, 4, 6]) == 5.0
```
The function median takes a list of numbers and calculates the median, which is the middle value of the two middle numbers, then returns the result.