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
The function `search` iterates through the list, updating the maximum observed value and the frequency of the current value. If the frequency meets the criteria, the function returns the current value. If no such value is found, `-1` is returned. 

This approach allows the function to be self-contained, using only the information contained in the input list `lst`, thus avoiding the need for any additional libraries or data structures.