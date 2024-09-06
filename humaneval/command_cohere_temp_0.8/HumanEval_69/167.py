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
The function initiates a frequency dictionary `freq` to tally how often each number appears in the list. The variable `max_val` is used to keep track of the highest value encountered during the process that meets the criteria of the problem. Ultimately, the function returns the greatest integer that satisfies the condition or -1 if no such number exists. 

This approach results in a straightforward solution that effectively addresses the problem. It is both reproducible and maintainable, making it a robust solution for this challenge.