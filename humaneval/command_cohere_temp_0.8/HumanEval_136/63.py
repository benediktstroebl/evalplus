```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0 and (n < positive or positive == float('-inf')):
            positive = n
        if n < 0 and (n > negative or negative == float('inf')):
            negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function iterates through the list, tracking the largest positive and smallest negative integer so far. Using `float('-inf')` and `float('inf')` allows us to handle the cases of no positive or negative integers in the list. The function returns a tuple (`a`, `b`) with the largest negative integer and the smallest positive integer, or `None` if there are none. 

The following examples illustrate how the function works:
```python
>>> largest_smallest_integers([2, 4, 1, 3, 5, 7])
(None, 1)

>>> largest_smallest_integers([])
(None, None)

>>> largest_smallest_integers([0])
(None, None)
``` 

This implementation follows the problem's guidelines and handles the specified edge cases.