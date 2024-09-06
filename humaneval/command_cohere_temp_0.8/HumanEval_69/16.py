```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n and (max_val < 0 or n > max_val):
                max_val = n
    return max_val if max_val > 0 else -1
```

This script defines a function `search` that solves the problem as outlined in the prompt. It iterates through the list, tracking the maximum value `max_val` and the frequency of each positive integer using the `count` method. If the frequency of an integer is greater than or equal to its value, `max_val` is updated. Finally, it returns the greatest integer if it meets the criteria; otherwise, it returns -1.