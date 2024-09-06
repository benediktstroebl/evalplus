```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > max_val:
            max_val = n
        if n >= freq:
            freq = n
    return max_val if freq >= max_val else -1
```

This Python script defines a function `search` to solve the given problem. It iterates through the list, updating the maximum value (`max_val`) and frequency (`freq`) as it goes. When `freq` is greater than or equal to the current integer `n`, it returns the maximum value `max_val`. If no such integer is found, it returns -1.