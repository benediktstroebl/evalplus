```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > max_val:
            max_val = n
        if n >= freq:
            freq = n
    return max_val if freq >= max_val else -1
```
The function `search` iterates through the list, updating the maximum observed value and the frequency of each value. If the frequency of a value is greater than or equal to the value itself, it returns this value, otherwise, it returns -1 if no such value is found in the list. 

Here is a simpler solution using Python's built-in `collections.Counter` for a slightly different perspective:
```python
def search(lst):
    c = collections.Counter(lst)
    return max(v for v in c.values() if v >= c[v]) if any(c[v] >= v for v in c) else -1
```
This solution uses the dictionary-like capabilities of `collections.Counter` to count the occurrences of each value in the list and then iterates over the values, returning the maximum if any of them are greater than or equal to their frequencies, and -1 otherwise.