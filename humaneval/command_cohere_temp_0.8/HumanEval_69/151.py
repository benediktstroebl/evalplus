```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > max_val:
            max_val = n
        if freq < n:
            freq = lst.count(n)
        if freq >= n:
            return n
    return -1
```

The function `search` iterates through the list, keeping track of the maximum value and its frequency. When the frequency meets or exceeds the current value, the function returns this value. If no such integer is found, the function returns -1. This solution adheres to the problem's guidelines and handles various scenarios. Test cases are essential to ensure its reliability for all possible inputs.