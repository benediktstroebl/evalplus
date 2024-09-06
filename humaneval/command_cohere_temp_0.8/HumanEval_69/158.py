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

The function `search` iterates through the list, keeping track of the variable `freq`, which records the frequency of the current integer in the list. It also keeps track of `max_val`, which records the maximum value in the list up until the current iteration. During each iteration, the function checks if the current integer has a frequency equal to or greater than itself. If so, it updates the `max_val` accordingly. If the maximum value encountered is equal to its own frequency (which is 1) and is still zero, this means there are no integers with a frequency greater than or equal to themselves, so the function returns -1. Otherwise, it returns the `max_val`.