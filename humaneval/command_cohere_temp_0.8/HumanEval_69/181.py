```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            max_val = max(max_val, n)
            freq = lst.count(n)
        if freq >= n:
            return n
    return -1
```

The function `search` iterates through the list `lst` and keeps track of the maximum value as it iterates through the list. It also keeps track of the frequency of each integer found in the list, using the `count` function. If the frequency of an integer is greater than or equal to the actual integer itself, it returns this integer, which is the answer to the problem statement. If no such integer is found, it returns `-1`.