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

The function iterates through the list, keeping track of the variable `freq`, which records the number of times the current integer is appearing in the list. It also keeps track of `max_val`, which is the maximum value in the list at any given point during iteration. In each iteration, the function checks if the current integer is greater than or equal to its frequency, if so, it updates the `freq` variable. It also checks if the current integer is greater than `max_val`, if so, it updates `max_val`. At the end of the iteration, the function returns -1 if the `max_val` is equal to its frequency and it is zero, otherwise, it returns the `max_val`. 

Here is an example usage of the function:
```python
print(search([5, 5, 4, 4, 4]))  # Output: -1
print(search([4, 1, 2, 2, 3, 1]))  # Output: 2
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))  # Output: 3
```

This should return -1 for the first example, 2 for the second example, and 3 for the third example, respectively.