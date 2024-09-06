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

The function iterates through the list, keeping track of both the maximum value **max_val** and the frequency of the current value **freq**. If the current number is greater than the current frequency, it updates the frequency. If it's also greater than **max_val**, it updates that as well.

At the end of the loop, if the maximum value is 0, it returns -1 if its frequency is also the same, as there are no larger values and this is the highest frequency value. Otherwise, it returns the maximum value.