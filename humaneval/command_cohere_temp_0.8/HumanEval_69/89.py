```python
def search(lst):
    freq, max_val = -1, 0 
    for val in lst:
        if val > max_val:
            max_val = val 
        if val == max_val and lst.count(val) >= val:
            freq = val 
    return max_val if freq >= 0 else -1
```

The function iterates through the list, keeping track of the highest value encountered `max_val`, and also tracking the frequency of the current value `freq`. If a value equals `max_val` and its frequency is greater than or equal to its value, `freq` is updated to this value. If no such value is found, the function returns -1.