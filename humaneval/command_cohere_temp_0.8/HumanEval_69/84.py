```python
def search(lst):
    freq, max_val = 0, max(lst)
    for n in lst:
        if n >= freq:
            freq = n
        if n > max_val:
            max_val = n
    return -1 if max_val == freq and max_val == 0 else max_val
```

The function iterates through the list, keeping track of both the maximum value `max_val` and the frequency of the current value `freq`. If a value exceeds the current maximum but has a frequency that's less than itself, it's discarded. This ensures that the answer is either the greatest value with a frequency equal to or greater than itself or `-1` if no such value exists.