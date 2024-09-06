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

The `search` function employs a dictionary (`freq`) to track the frequency of each number in the list. The maximum value that qualifies under the given conditions is computed initially, then each number is checked against this maximum value, and finally, any qualifying number is returned. 

The `max_val` variable is initialized to zero and updates as the loop progresses, representing the maximum frequency seen so far. The final maximum value is adjusted to be no lower than 1, effectively handling the corner case where the list might not contain any positive integers. 

This solution allows for a straightforward and efficient identification of the desired integer.