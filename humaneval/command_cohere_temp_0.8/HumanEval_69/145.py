```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n <= 0:
            continue
        freq[n] = freq.get(n, 0) + 1
        max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```

This script defines a function `search` that solves the problem as described in the markdown code block. It uses a dictionary `freq` to store the frequency of each number in the list. Then, it iterates over the list and updates the frequency of each element. Afterward, it checks if the maximum frequency value is greater than or equal to 1 and returns the corresponding number if possible; otherwise, it returns -1.