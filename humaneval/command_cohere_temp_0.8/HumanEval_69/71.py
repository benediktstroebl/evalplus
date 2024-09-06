```python
def search(lst):
    freq, max_val = dict(), 0
    for n in lst:
        if n > 0:
            freq[n] = freq.get(n, 0) + 1
            max_val = max(max_val, freq[n])
    return -1 if max_val < 1 else max(n for n in freq if freq[n] >= n)
```
The function initiates a frequency dictionary `freq` to tally how often each number appears in the list. The variable `max_val` is used to denote the maximum frequency of any number greater than zero. The function then iterates through the list, updating the `freq` dictionary and `max_val` where appropriate. Finally, the function returns -1 if `max_val` is less than 1, indicating that no number meets the criteria. If `max_val` is greater than or equal to 1, it returns the highest number that meets the criteria, namely the number with the greatest frequency that's also greater than zero. 

Here is a simpler alternative problem solution using `heapq` module:
```python
def search(lst):
    freq = collections.Counter(lst)
    return -1 if max(freq.values()) < 1 else max(n for n in freq if freq[n] >= n, default=-1)
```
This alternative approach uses the `collections.Counter()` to create a dictionary of frequencies of elements in the list. The `max()` function is used to find the maximum frequency value, and the `max()` with a dictionary comprehension is used to find the element with a frequency equal to or greater than itself. The `default=-1` argument ensures that any nonexistent values yield the default return value of -1. This solution is more concise but perhaps slightly less intuitive than the previous one.