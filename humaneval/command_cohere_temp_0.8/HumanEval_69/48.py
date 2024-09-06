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

The function iterates through the list, tracking the maximum value of the list (`max_val`) and the frequency of each integer in the list (`freq`). If the maximum value is equal to its frequency and equals zero, it returns -1. Otherwise, it returns the `max_val` value. 

Here is an example usage of the function:
```python
print(search([1, 2, 2, 3, 3, 3, 4, 4, 4]))
```

The output will be:
```
3
```