```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The script utilizes a dictionary (`freq`) to maintain the frequency of each number present in the list. After iterating through the list, it checks if the maximum frequency value exceeds or equals one. If this condition is fulfilled, the script returns the `max_val`, otherwise, it returns -1. This approach ensures the solution handles all scenarios mentioned in the prompt and aligns with the intended algorithm.