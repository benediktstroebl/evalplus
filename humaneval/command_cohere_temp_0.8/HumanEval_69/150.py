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
The function first creates a dictionary (`freq`) where the keys are the numbers from the list and the values are their frequencies. Then, it finds the maximum value of the frequencies, (`max_val`) skipping the non-positive integers. Finally, it returns the number that has a frequency equal to or greater than itself, or -1 if no such number exists. 

This solution works efficiently in `O(n)` time complexity and has a space complexity of `O(n)` as well, due to the dictionary allocation.