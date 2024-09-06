```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The code defines a function `search` taking a list of positive integers as input. It initializes a dictionary `freq` to store integer frequencies and a maximum value `max_val` to track the largest frequency encountered. Each number in the list is iterated through, updating its frequency and recomputing `max_val` as necessary. Ultimately, the function returns `-1` if `max_val` is less than 1 (indicating no positive integer has a frequency >= itself) and the maximum value otherwise.