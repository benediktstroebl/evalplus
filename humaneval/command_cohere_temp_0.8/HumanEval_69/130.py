```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n and (max_val < 0 or n > max_val):
                max_val = n
    return max_val if max_val > 0 else -1
```

The function `search` iterates through the list `lst`, tracking the maximum value (`max_val`) and the frequency of each positive integer. When the frequency of an integer is greater than or equal to its value, the function updates `max_val` and returns the new maximum. If no such integer is found, it returns -1. 

This solution has a time complexity of O(n), where n is the length of the input list, since it requires iterating through the list once to find the maximum value that meets the criteria.