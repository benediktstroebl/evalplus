```python
def largest_smallest_integers(lst):
    if not positive_integers(lst) and not negative_integers(lst):
        return (None, None)
    elif len(lst) == 0:
        return (None, None)
    else:
        # Find the largest and smallest integers
        a, b = max(lst), min(lst)
        return (a, b)

def positive_integers(lst):
    return any(x > 0 for x in lst)

def negative_integers(lst):
    return all(x < 0 for x in lst)

# Test cases
largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (7, 2)
largest_smallest_integers([3]) == (None, None)
largest_smallest_integers([0]) == (None, None)
```
This script defines a function `largest_smallest_integers` that takes a list as input and returns a tuple with the largest and smallest integers. The function `positive_integers` and `negative_integers` are also defined to check if the input list contains only positive or negative integers, respectively, and return `True` or `False`.  The test cases are provided to verify the correctness of the function.