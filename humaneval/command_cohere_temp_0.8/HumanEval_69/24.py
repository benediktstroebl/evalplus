```python
def search(lst):
    freq, max_val = -1, 0 
    for val in lst:
        if val > max_val:
            max_val = val 
        elif val == max_val and lst.count(val) >= val:
            freq = val 
    return max_val if freq >= max_val else -1
```

This script defines a function 'search' which iterates through the list 'lst' and keeps track of the maximum value in the list 'max_val'. Additionally, it keeps track of the frequency of the current maximum value encountered, denoted by 'freq'. If a value exceeds the current 'max_val', the 'max_val' is updated. If the current value equals 'max_val' and its frequency is greater than or equal to its value, 'freq' is updated. Finally, the function returns the 'max_val' if its corresponding frequency is at least equal to its value, and -1 otherwise. 

Would you like to test this script? Any additional help welcome!