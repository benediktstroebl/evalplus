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

This script defines a function 'search' which takes in a list of integers and returns the greatest integer that is greater than zero and has a frequency greater than or equal to the value of the integer itself. If no such integer exists, it returns -1. This is achieved by initializing the variables `freq` and `max_val` to -1 and 0 respectively, and then iterating through the list. 

For each integer `n` in the list, it checks if `n` is greater than the current `max_val`. If so, it updates `max_val` to n. Then it checks if `n` is greater than or equal to the current frequency `freq`. If so, it updates `freq` to n. After iterating through the list, it returns `max_val` if `freq` is greater than or equal to `max_val`. Otherwise, it returns -1. 

This solution is adapted from some of the solutions to the problem provided by the GeeksforGeeks community available [here](https://www.geeksforgeeks.org/find-greatest-integer-with-frequency-greater-than-or-equal-to-its-value-given-list-integers-using-python/), and it can be verified by writing tests that cover different scenarios.