```python
def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > 0:
            freq = lst.count(i)
            if freq >= i and (max_val < 0 or i > max_val):
                max_val = i 
    return max_val if max_val > 0 else -1
```

The function `search` iterates through the list `lst`, counting the frequency of each integer. If an integer is greater than zero and its frequency is greater than or equal to the integer itself, the variable `max_val` is updated to this integer, if it's even greater than the current `max_val`. Ultimately, `max_val` will hold the greatest integer that satisfies the conditions of the problem, or -1 if no such integer exists.