```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > max_val:
            max_val = n
        if n >= freq:
            freq = n
    return -1 if max_val == 0 else max_val
```

The function `search` iterates through the list `lst`, tracking the maximum value found so far (`max_val`) and the frequency of the current number. If the current number is greater than the `max_val`, `max_val` is updated. If the current number is equal to or greater than its own frequency, `freq` is updated. 

This approach ensures that each number is checked against both criteria in a single pass of the list. Also, the -1 return for an empty max_val set is assumed in the md.