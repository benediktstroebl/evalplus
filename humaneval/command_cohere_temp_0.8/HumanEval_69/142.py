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
The function `search` iterates through the list `lst`, tracking the maximum value encountered as `max_val`, and also keeping track of the least frequent integer encountered so far as `freq`. If the current integer has a frequency greater than or equal to its own value, it is returned as the solution. If no such integer is found, the function returns -1. This solution assumes that the list `lst` only contains positive integers. 
This approach is linear time complexity `O(n)` where `n` is the length of the input list.