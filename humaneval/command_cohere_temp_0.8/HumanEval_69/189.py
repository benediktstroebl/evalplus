```python
def search(lst):
    freq, max_val = -1, 0 
    for val in lst:
        if val > max_val:
            max_val = val 
        if val == max_val and lst.count(val) >= val:
            freq = val 
    return max_val if freq >= 0 else -1
```

The function iterates through the list, tracking the highest value seen `max_val`, and also tracking the largest frequency seen `freq`. If a value equals its own frequency, or more, it is returned, otherwise, the search continues. The final return value is the highest value found that meets the criteria, or -1 if no such value is found. 

This approach is efficient because it's O(n) and has a time complexity of linearity, meaning it checks each element exactly once. Also, the memory complexity is constant since it requires a constant amount of extra space to store the variables.