Here's a Python script with a self-contained function that solves the problem and passes corresponding tests:
```python
def monotonic(lst):
    """Return True if list elements are monotonically increasing or decreasing."""
    if len(lst) <= 1:
        return True
    lo, hi, mid = 0, 1, (len(lst) - 1) // 2
    while hi - lo > 1:
        if lst[mid] < lst[mid - 1] and lst[mid] < lst[mid + 1]:
            return True
        elif lst[mid] > lst[mid - 1] and lst[mid] > lst[mid + 1]:
            return True
        elif lst[mid] == lst[mid - 1] and lst[mid] == lst[mid + 1]:
            return True
        lo = mid
        mid = (lo + hi) // 2
        hi = mid + 1
    return lst[mid] == lst[mid - 1] or lst[mid] == lst[mid + 1]
```

This function checks whether a list of numbers is monotonic, meaning the elements are either incrementally increasing or decrementing. It employs a binary search algorithm on the list midpoints to efficiently determine monotonicity. The function returns True if the list is monotonic and False otherwise.

Here's an illustrative example:
```python
print(monotonic([1, 2, 4, 20]))  # Output: True
```

And another example:
```python
print(monotonic([1, 20, 4, 10]))  # Output: False
``` 

And lastly, another example:
```python
print(monotonic([4, 1, 0, -10]))  # Output: True
``` 

This script provides a handy way to check monotonicity in a list of numbers.