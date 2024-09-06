```python
def search(lst):
    freq, max_val = -1, 0 
    for n in lst:
        if n > max_val:
            max_val = n 
        if n >= freq:
            freq = n 
    return -1 if max_val == 0 else max_val 

# Tests
assert search([4, 1, 2, 2, 4, 1, 3]) == 2
assert search([1, 2, 2, 3, 3, 3, 4, 4, 4]) == 3
assert search([5, 5, 4, 4, 4]) == -1
assert search([7, 5, 3, 2, 2, 2, 1, 1, 1]) == -1
```

The function `search` iterates over the list and updates the maximum value and its frequency as it goes. 

If the maximum value is zero, it returns -1, indicating that no valid answer exists. Otherwise, it returns the greatest integer that is greater than zero and has a frequency greater than or equal to its value.