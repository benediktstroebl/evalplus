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

The function iterates through the list, keeping track of the highest value encountered (`max_val`) and whether this highest value has a frequency equal to or greater than itself. If no such integer is found, the function returns -1. If such an integer is found, it returns the maximum value.