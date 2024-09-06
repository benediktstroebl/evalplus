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

The function iterates through the list, keeping track of both the maximum value `max_val` and the frequency of the current value `freq`. When a number is greater than or equal to its frequency, the frequency is updated. If the maximum value is equal to its own frequency and zero, meaning there is no integer satisfying the condition, the function returns -1. Otherwise, it returns the greatest integer that satisfies the problem's condition. 

This approach is linear time and assumes the list is sorted. If the list is not sorted, the algorithm may produce incorrect results.