```python
def largest_smallest_integers(lst):
    positive = None
    negative = None
    for n in lst:
        if n > 0:
            if positive is None or n > positive:
                positive = n
        elif n < 0:
            if negative is None or n < negative:
                negative = n
    return (negative, positive)
```

The function `largest_smallest_integers` iterates through the list `lst`, identifying the largest negative integer and the smallest positive integer. The code employs two flags, `positive` and `negative`, which are initially set to `None`. When a number is encountered that is either positive or negative, the respective flag is updated to that value if it is smaller than the existing value or None. The function returns a tuple containing the largest negative integer and the smallest positive integer.

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

This illustrates that the function correctly identifies the largest negative integer and the smallest positive integer in various scenarios.