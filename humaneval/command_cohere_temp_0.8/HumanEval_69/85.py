```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n:
                max_val = max(max_val, n)
        if freq > 0 and max_val >= 0:
            return max_val
    return -1
```
The function iterates through the list, tracking the frequency of each integer. When the frequency of an integer equals or exceeds itself, it compares this value with the current maximum and updates max_val if needed. Thus, it identifies the maximum value with a frequency proportionate to or greater than itself. If no such integer is found, it returns -1.