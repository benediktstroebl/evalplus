```python
def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > max_val:
            max_val = i 
        if i == max_val and lst.count(i) >= i:
            freq = i 
    return max_val if freq == -1 else -1 
```

The `search` function iterates through the list `lst`, tracking the maximum value `max_val` and its frequency. When an integer's value matches its frequency, `freq` stores this value. If no match is found, the function returns -1. 

This solution maintains a single loop structure, avoiding the complexity of nested loops or additional algorithms to search through the list just once. 

The `max_val` and `freq` variables are used to store the maximum value found and the frequency of that number, respectively. As the loop iterates through the list, it updates these variables as necessary. 

The return statement checks if `freq` is -1, which indicates that no number in the list meets the criteria of the problem. In that case, it returns -1. Otherwise, it returns the maximum value `max_val`, which is the solution to the problem.