```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n:
                if n > max_val: max_val = n
    return -1 if max_val == 0 else max_val
```
The function `search` iterates through the list `lst`, tracking the frequency of each integer. When it encounters a positive integer `n`, it compares `n` with the frequency of its occurrence (`freq`). If this frequency is greater than or equal to `n`, it checks if `n` is the maximum value encountered so far (`max_val`). If it is, the value is updated accordingly. The function returns -1 if no suitable integer is found, implying no integer satisfies the conditions.