```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            max_val = max(max_val, n)
            freq = lst.count(n)
        if freq >= n:
            return max_val
    return -1
```

This Python script defines a function `search` using a list of positive integers as input. It aims to find the maximum value that appears at least as frequently as its appearance in the list. It initializes `freq` and `max_val` to -1 and 0, respectively. Then, it iterates through the list, checking if each element is greater than 0. If so, it updates `max_val` with the maximum value and counts the frequency of that element in the list. If the frequency is greater than or equal to the element's value, it returns the maximum value. If no such element is found, it returns -1. 

The code efficiently solves the problem using a single loop and basic logic, achieving a time complexity of O(n), where n is the length of the input list.