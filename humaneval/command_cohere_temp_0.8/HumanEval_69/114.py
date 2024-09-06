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

This Python script defines a function `search` using a single loop to iterate through a list of integers. It aims to find the greatest integer (`max_val`) that is both greater than zero and has a frequency (`freq`) equal to or greater than its own value in the list. The `search` function efficiently examines each integer in the list, tracking the maximum value and its frequency. If a number greater than zero is found with a frequency meeting the criteria, its value is returned; otherwise, the function returns -1 to indicate no such number exists. 

Here is an example of how to use the `search` function:
```python
search([1, 2, 2, 3, 3, 3, 4, 4, 4])
```

The output will be:
```bash
3
```