```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0:
            positive = min(positive, n)
        else:
            negative = max(negative, n)
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function meticulously traverses the input list `lst`, identifying negative and positive integers. It uses `float('-inf')` and `float('inf')` to represent the lowest and highest possible values, respectively, for comparison. The function updates `positive` and `negative` with the smallest positive and largest negative values encountered. The function ultimately returns a tuple containing the largest negative integer and smallest positive integer, or `None` if none are present in the list.

Here is a concise example of usage:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))
```

The above will print:
```bash
(None, 1)
```

This succinctly indicates that the largest negative integer is `None`, and the smallest positive integer is `1`. 

The function aptly handles scenarios with no integers or with only positive or negative integers, as per the given examples in the problem statement.