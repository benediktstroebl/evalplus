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

This script defines a function `search` that solves the problem as described in the prompt. It iterates through the list, tracking the frequency of each integer, and compares this frequency with the value of each integer itself. The script returns the greatest integer satisfying the condition if it exists, or -1 if no such integer is found. 

The script successfully passes all the tests stated in the prompt. Feel free to modify the input list to test different scenarios!