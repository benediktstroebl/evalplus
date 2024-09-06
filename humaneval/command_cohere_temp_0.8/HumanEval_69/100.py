```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The code defines a function `search` taking a list of positive integers as input. It initializes a dictionary `freq` to store the frequency of each number and a variable `max_val` to store the maximum frequency value. Then, it iterates through the list, updating the frequency of each number and the `max_val`. Afterward, it checks if the maximum frequency is less than 1, in which case no number meets the criteria, and returns -1. Otherwise, it iterates through the `freq` dictionary to find the maximum value of the number with a frequency greater than or equal to itself and returns it.