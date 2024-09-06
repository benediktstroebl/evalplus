```python
def search(lst):
    freq, max_val = 0, max(lst)
    for n in lst:
        if n >= freq:
            freq = n
        if n > max_val: 
            max_val = n
    return -1 if max_val == freq and max_val == 0 else max_val
```

The function iterates through the list, keeping track of the variable `freq`, which records the frequency of the current integer, and `max_val`, which is gradually updated to the maximum value in the list. If a number is greater than or equal to its frequency, the frequency is updated; simultaneously, if a number is greater than `max_val`, `max_val` is updated. 

At the end, the variable `max_val` is checked for being equal to `freq` and both being zero, which is the condition when there is no number greater than or equal to its frequency in the list. The function returns -1 if this condition is true, otherwise, it returns `max_val`.