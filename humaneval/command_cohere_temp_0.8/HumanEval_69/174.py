```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```

The function initiates a frequency dictionary `freq` to tally how often each integer appears in the list. Subsequently, it determines the maximal value (`max_val`) among those whose frequency equals or surpasses their own value. If no such integer is found, the function returns -1. Otherwise, it returns the greatest integer satisfying this condition.

This Python script aligns with the problem statement and stands ready for further testing. Feel free to adapt the function to fulfill any specific requirements you may have. If you have additional questions or further insights, please don't hesitate to ask! Enjoy your day ahead!