```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > max_val:
            max_val = n
        if n >= freq:
            freq = n
    return max_val if freq >= max_val else -1
```

This script defines a function `search` that solves the problem as outlined in the markdown code block. It iterates through the list, updating the `max_val` and `freq` variables to the desired values. Finally, it returns the result based on the conditions mentioned in the problem description.