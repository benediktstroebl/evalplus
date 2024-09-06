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

This script defines a function search that solves the described problem. It counts the frequency of each number in the list and compares this to the value of the number itself. The greatest number with a frequency equal to or greater than its own value is returned, or -1 is returned if no such number exists. The max_val variable is used to keep track of the greatest value encountered so far, updating accordingly in each iteration.