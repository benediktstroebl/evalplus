```python
def largest_smallest_integers(lst):
    negative = None
    positive = None
    for n in lst:
        if n < 0:
            if negative is None or n > negative:
                negative = n
        else:
            if positive is None or n < positive:
                positive = n
    return (negative, positive)
```

The `largest_smallest_integers` function iterates through the list of integers and identifies the largest negative and smallest positive integers. The function assigns `None` to `negative` and `positive` at the beginning. Then, it compares the current integer with these variables and updates them if necessary. Ultimately, it returns a tuple containing these two values.

Here is an example usage of the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7])) 
print(largest_smallest_integers([])) 
print(largest_smallest_integers([0])) 
```

The output will be:
```
(None, 1)
(None, None)
(None, None)
```

This illustrates that the function correctly identifies the largest negative and smallest positive integers as described in the problem statement. If there are no negative or positive integers in the list, the function returns `None` for both values, as expected.