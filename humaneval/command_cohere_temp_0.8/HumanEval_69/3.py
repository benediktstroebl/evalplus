```python
def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > 0:
            max_val = i if i > max_val else max_val 
            if i == max_val and lst.count(i) >= i:
                freq = i 
    return max_val if freq == max_val else -1
```

This Python script defines a function `search` to solve the given problem. It iterates through the list, tracking the maximum value (`max_val`) and its frequency. When an integer is greater than `max_val`, it updates both `max_val` and frequency. If an integer has a frequency equal to or greater than itself, it returns the `max_val`. If no such integer is found, it returns -1.