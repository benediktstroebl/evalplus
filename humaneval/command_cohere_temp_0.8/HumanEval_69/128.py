```python
def search(lst):
    freq, max_val = -1, 0 
    for val in lst:
        if val > max_val:
            max_val = val 
        elif val == max_val and lst.count(val) >= val:
            freq = val 
    return max_val if freq == -1 else -1 
```

The function iterates through the list, keeping track of the highest value encountered (`max_val`) and its frequency. When a number is equal to `max_val`, we check if its frequency is greater than or equal to the number itself. If such a number is not found, the frequency will remain `-1`, and the function will return either `max_val` or `-1` accordingly.