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

The function iterates through the list, keeping track of the maximum value while also counting the frequency of each number. If the condition is met where the maximum value is equal to its frequency and it's zero, meaning there is no integer that meets the requirement, the function returns -1. Otherwise, it returns the greatest integer that meets the criterion.