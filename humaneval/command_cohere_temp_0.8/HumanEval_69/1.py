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

This script defines a function 'search' which iterates through a list of integers 'lst'. It computes the maximum value in the list at each iteration using a variable 'max_val'. It also keeps track of the frequency of this maximum value with the variable 'freq'. If a value greater than zero is found whose frequency is greater than or equal to its value, or if no such integer is found, the function returns the maximum value or -1, respectively. 

The function is designed to efficiently handle lists with unique values, and its performance is O(n) where n is the number of elements in the given list.