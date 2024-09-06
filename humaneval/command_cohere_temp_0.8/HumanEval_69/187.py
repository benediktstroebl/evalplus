```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```

The function iterates through the list and uses a dictionary `freq` to store the frequency of each integer. The maximum value is tracked while looping through, and the function returns -1 if the maximum frequency value is less than 1. If it is, the function searches for an integer in the dictionary where the frequency is greater than or equal to the integer itself.