```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            max_val = max(max_val, n)
            if n >= freq:
                freq = n
    return max_val if freq >= max_val else -1
```

This Python script defines a function `search` which solves the problem statement. It iterates through the list, updating the maximum value (max_val) and simultaneously checking the frequency of each integer in the list. If the frequency is greater than or equal to the integer itself, it returns that integer. Otherwise, it returns -1, indicating that no such integer exists in the list.