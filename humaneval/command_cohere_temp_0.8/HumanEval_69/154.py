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
The `search` function iterates through the list `lst`, updating the `max_val` and `freq` variables whenever necessary. If a number greater than `max_val` is encountered, `max_val` is updated. If a number greater than or equal to its frequency is encountered, `freq` is updated. After iterating through the list, the function returns the `max_val` if `freq` is greater than or equal to `max_val`. Otherwise, it returns `-1`.