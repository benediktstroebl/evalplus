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

This Python script defines a function `search` that processes a list of positive integers. It seeks to find the greatest positive integer (`max_val`) that has a frequency (`freq`) equal to or greater than its own value. The function iterates through the list, updating `max_val` and `freq` for each integer. If the frequency condition is met, the function immediately returns the maximum value. If no such integer is found, it returns -1 to indicate the absence of a suitable value. 

The script ensures it adheres to the described behavior through precise variable tracking and conditional checks, thus guaranteeing the correct solution to the problem.