```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            freq = lst.count(n)
            if freq >= n and (max_val < 0 or n > max_val):
                max_val = n
    return max_val if max_val > 0 else -1
```

This script defines a function 'search' that solves the problem as described in the prompt. It uses a nested loop to iterate through the list 'lst' of positive integers, counting the frequency of each integer. If the frequency of an integer is greater than or equal to the value of the integer itself, it updates the max_val to that integer's value. Finally, it returns the max_val if such a value exists, or -1 if no such value is found.

The script assumes the input list 'lst' contains only positive integers and that at least one such integer is present.