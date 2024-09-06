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
The function iterates through the list `lst`, tracking the maximum value encountered as `max_val`, and the frequency of the current value as `freq`. If the frequency of an integer is greater than or equal to its current value, we update `max_val`. After checking all integers, return `max_val` if valid, otherwise `-1` if no such integer is found. 

This approach allows the function to efficiently identify the greatest integer that satisfies the condition and return the answer directly without any complex data manipulation.