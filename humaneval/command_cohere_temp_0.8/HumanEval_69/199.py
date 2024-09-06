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

This script defines a Python function `search` that takes a list of integers as input and returns the greatest integer that meets the conditions stated in the problem prompt. The function iterates through the list, keeping track of the maximum integer value (`max_val`) and its frequency. If a value greater than `max_val` is encountered, `max_val` is updated. If a value equal to `max_val` is encountered and its frequency is greater than or equal to its value, the function updates the `freq` variable with the value. 

After processing the entire list, the function returns the maximum value if its frequency meets the conditions; otherwise, it returns -1 to indicate that no such integer exists in the list. 

This solution is self-contained and can be executed directly in Python to test and validate its behavior against the provided examples in the problem statement.