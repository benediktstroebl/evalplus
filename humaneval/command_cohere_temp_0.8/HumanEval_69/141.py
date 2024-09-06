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

This script provides a `search` function that solves the problem statement. It acts as follows:
1. Initialize `freq` and `max_val` to -1 and 0 respectively, the former to record the frequency of the maximum appearing integer, and the latter to record the maximum appearing integer. 
2. Iterate through the list, if the current integer is greater than `max_val`, update `max_val` to the current integer. 
3. If the current integer is equal to `max_val`, check if its frequency is greater than or equal to the integer itself. If so, update the `freq` variable. 
4. Return `max_val` if `freq` is -1, this means that there exists an integer greater than 0 whose frequency is greater than or equal to itself. Otherwise, return -1, as no such integer exists. 

Thus this script solves the problem using two variables to efficiently keep track of the maximum integer and its corresponding frequency.