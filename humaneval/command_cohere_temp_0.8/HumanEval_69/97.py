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

This Python script defines a function `search` that solves the problem you described. It iterates through the list, maintaining a frequency count and keeping track of the maximum value encountered (max_val). The function returns -1 if the maximum frequency is less than 1, indicating that no valid answer is found. Otherwise, it returns the largest integer that meets the criteria, by filtering the freq dictionary for elements whose frequency is at least equal to their value.