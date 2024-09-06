```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > max_val:
            max_val = n
        if n >= freq:
            freq = n
    return -1 if max_val == 0 else max_val if freq >= max_val else -1
```

The function `search` iterates through the list, updating the `max_val` and `freq` variables accordingly. If no integer greater than zero meets the requirement, the function returns -1. 

This solution focuses on simplicity and readability. If you'd like a more optimized approach, feel free to ask. Let me know if you'd like me to explain any part of the code further.