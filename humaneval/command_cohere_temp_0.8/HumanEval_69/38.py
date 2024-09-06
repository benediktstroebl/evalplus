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
The function `search` iterates through the list `lst` and simultaneously keeps track of the maximum value encountered (`max_val`) and the frequency of the current value. If a value exceeds the current maximum and its frequency is greater than or equal to its value, we return this value. If no such value is found, we return -1. This approach ensures that each potential answer is checked in the minimum number of iterations.