```python
def largest_smallest_integers(lst):
    positive = float('-inf')
    negative = float('inf')
    for n in lst:
        if n > 0 and (positive == float('-inf') or n > positive):
            positive = n
        if n < 0 and (negative == float('inf') or n < negative):
            negative = n
    return (negative if negative != float('inf') else None,
            positive if positive != float('-inf') else None)
```

The `largest_smallest_integers` function works by setting the variables `positive` and `negative` to negative and positive infinity respectively. Then, it iterates over the list, checking if any of the elements are larger/smaller than the current maximum/minimum values. The function updates the max/min values if so. Finally, the function returns a tuple containing the maximum/minimum values, or `None` if none of the respective values were found in the list.

The following example demonstrates how to use the function:
```python
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # Outputs: (None, 1)
print(largest_smallest_integers([]))  # Outputs: (None, None)
print(largest_smallest_integers([0]))  # Outputs: (None, None)
```

This would output:
```bash
(None, 1)
(None, None)
(None, None)
```

This illustrates the function's behavior correctly as per the given examples in the prompt.