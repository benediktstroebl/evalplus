```python
def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > max_val:
            max_val = i 
        if i >= freq:
            freq = i
    return max_val if freq >= max_val else -1
```
The function iterates through the list, updating the maximum observed value and the frequency of each value. If the frequency of an integer is greater than or equal to its current value, we return the maximum value observed, otherwise, we return -1. This works because the maximum value we observe must necessarily have a frequency <= than the maximum value, so if we didn't find any integer with a frequency >= itself, we know the answer is -1.