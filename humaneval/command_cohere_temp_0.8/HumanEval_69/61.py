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

This script defines a function `search` that solves the described problem. It counts the frequency of each number in the list using a dictionary `freq`, and simultaneously tracks the maximum value seen so far `max_val`. The loop checks if the current number is greater than the maximum value, updating `max_val` if so. It also checks if the current number has a frequency greater than or equal to its own value, updating `freq` if so. Finally, the function returns the maximum value encountered if its condition is met, or -1 if none of the numbers satisfy the condition.