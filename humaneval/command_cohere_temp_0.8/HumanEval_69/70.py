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
The function first builds a dictionary (`freq`) of integers from the list and their respective frequencies. Then, it maximizes over the integers in the list with frequencies greater than or equal to themselves, or returns -1 if no such integer exists. The maximization is done via a generator expression within the max function.