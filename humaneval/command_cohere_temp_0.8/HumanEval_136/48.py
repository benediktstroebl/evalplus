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

The `largest_smallest_integers` function works by setting initial values for `positive` and `negative` to negative and positive infinity, respectively. This allows us to efficiently update the values as we iterate through the list, as any integer value will be finite compared to infinity.

The loop iterates over the list, checking if each integer is positive. If it is, it updates `positive` only if the current value is smaller than the candidate or inititialized to -inf. The same logic applies to negative integers and the `negative` variable.

Finally, the function returns a tuple containing the largest negative integer (or None if there are no negative integers) and the smallest positive integer (or None if there are no positive integers).

The following examples illustrate the behavior of the function:
```python
>>> largest_smallest_integers([2, 4, 1, 3, 5, 7])
(None, 1)

>>> largest_smallest_integers([])
(None, None)

>>> largest_smallest_integers([0])
(None, None)
``` 

This solution meets the specified requirements and handles edge cases appropriately.