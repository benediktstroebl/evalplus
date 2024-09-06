```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n <= 0:
            continue
        freq[n] = freq.get(n, 0) + 1
        max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(max_val, max(lst))
```

The function first creates a dictionary `freq` that holds the frequency of each number in the list. Then, it finds the maximum frequency of any number in the list, initially assuming it will be the list maximum itself. However, if this maximum frequency is less than 1, it means that no number in the list has a frequency equal to or greater than itself, so in this case, we return -1. If a number with a frequency equal to or greater than itself is found, we return this number if it's larger than the current maximum, or the maximum of the list if not.