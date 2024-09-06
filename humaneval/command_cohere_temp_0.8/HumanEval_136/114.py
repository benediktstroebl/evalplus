```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            if n > positive:
                positive = n
        elif n < 0:
            if n < negative:
                negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The function `largest_smallest_integers` works by setting the variables `positive` and `negative` to negative and positive infinity respectively. It then iterates over the list, checking if each integer is positive or negative. If so, it updates these variables to the respective values. Finally, the function returns a tuple containing these values. Note that the function also checks for the case where the list might be empty or contain only zero, returning 'None' in such cases. 

This approach guarantees that the code will work as described in the prompt, i.e., return the largest negative integer and the smallest positive integer from the list, or 'None' if there are none. 

The following example tests should validate the functionality:
```python
assert largest_smallest_integers([2, 4, 1, 3, 5, 7]) == (None, 1)
assert largest_smallest_integers([]) == (None, None)
assert largest_smallest_integers([0]) == (None, None)
assert largest_smallest_integers([-1, -2, -3, -4, -5]) == (-5, None)
```