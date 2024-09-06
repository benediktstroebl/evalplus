```python
def search(lst):
    freq, max_val = -1, 0 
    for val in lst:
        if val > max_val:
            max_val = val 
        if val >= freq:
            freq = val 
    return max_val if max_val >= 0 and max_val >= freq else -1
```

The function `search` iterates through the list, updating the maximum observed value `max_val` and the frequency of the current value `freq`. If a value greater than zero meets the criterion, it returns this value. Otherwise, it returns -1, indicating that no such number exists.