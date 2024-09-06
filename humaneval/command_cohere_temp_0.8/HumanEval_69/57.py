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

The function iterates through the list, keeping track of the variable `freq`, which records the frequency of the current integer in the list, and `max_val`, which is gradually updated to the maximum value in the list. If a number is greater than or equal to its frequency, `freq` is updated accordingly.

At the end of the iteration, if the maximum value in the list is equal to its frequency and is zero, indicating no other integer has a frequency greater than or equal to itself, the function returns -1, indicating that no valid answer is found. Otherwise, it returns the maximum value. 

This algorithm has a time complexity of O(n) and is a straightforward approach for solving this problem.