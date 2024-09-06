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

This script defines a function `search` that solves the problem as stated in the prompt. It iterates through the list, updating the maximum value and frequency of elements, and returns the result accordingly. This solution is efficient with a time complexity of O(n) since it requires two passes over the input list.