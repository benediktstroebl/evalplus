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

The function iterates through the list, keeping track of the highest value and its frequency. When a new maximum is found, it checks if its frequency is greater than or equal to the value. If so, the maximum value is returned if it meets the condition, or -1 is returned if no such integer is found. This is done in a time complexity of O(n), where n is the length of the passed list. 

Would you like to test the script with example cases to see if it passes? This can be done to ensure that the function is behaviourally correct.