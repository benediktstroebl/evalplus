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
The function iterates through the list, keeping track of the maximum value encountered (`max_val`) and the frequency of the current value. If the frequency is greater than or equal to the current value, we return the value immediately. If no such integer is found, the function returns -1.