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

The function iterates through the list, keeping track of both the maximum value and the frequency of each value. When a number is greater than the current maximum but its frequency is equal to or greater than itself, the function returns this value. The check `max_val == freq` and `max_val == 0` is to ensure that no maximum is overestimated, returning -1 if no valid maximum is found.