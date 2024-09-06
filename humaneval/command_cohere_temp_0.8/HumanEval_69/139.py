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
The `search` function iterates through the list `lst`, tracking the maximum value encountered (`max_val`) and its frequency (`freq`). It returns the maximum value if its frequency is greater than or equal to its value, otherwise, it returns `-1` to signify no such number exists. This approach ensures the function efficiently solves the problem in a single pass.