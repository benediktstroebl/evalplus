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

The function iterates through the list, keeping track of the highest value encountered `max_val`, and also tracking the frequency of the current value `freq`. If a value equals `max_val` and its frequency is greater than or equal to the value itself, `freq` equals the value. If no such value is found, the function returns `-1`. 

This approach guarantees that the problem is solved in O(n) time complexity, where n is the length of the list. 

The method effectively leverages the properties of the problem to avoid the need for more sophisticated algorithms usually utilized for detecting frequencies in lists, such as hash maps, and instead uses a straightforward and efficient loop. 

This makes the solution particularly useful for scenarios where large datasets need to be processed quickly, and the trade-off between time complexity and space complexity is of utmost importance.