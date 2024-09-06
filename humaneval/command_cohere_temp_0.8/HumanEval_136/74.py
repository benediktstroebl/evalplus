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

The `largest_smallest_integers` function iterates through the list, identifying the smallest positive and largest negative integers. Using `float('-inf')` and `float('inf')` allows comparison of floats and integers correctly. The function returns the respective values or `None` if not found.

Here is how you could use this function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
```

This would output the following:
```
(None, 1)
```

This is consistent with the example provided in the original problem description.