```python
def search(lst):
    freq, max_val = -1, 0 
    for n in lst:
        if n > max_val:
            max_val = n 
        if n >= freq:
            freq = n 
    return max_val if max_val >= 0 and max_val >= freq else -1
```
The `search` function iterates through the list `lst`, tracking the maximum value encountered 'max_val' and the frequency of the current value 'freq'. If a value greater than zero exceeds or equals its frequency, it returns this value, otherwise, it returns -1. 

You can test the function by calling `search([list_of_integers])`. Ensure the `max_val` and `freq` variables are updated correctly when a new value is encountered and that `max_val` is correctly updated.