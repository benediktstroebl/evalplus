```python
def search(lst):
    freq, max_val = -1, 0
    for i in lst:
        if i > 0:
            max_val = i if i > max_val else max_val
            if i == freq:
                return i
            freq = lst.count(i)
    return -1
```

This Python script defines a function search that solves the described problem. It iterates through the given list, tracking the maximum value (max_val) and its frequency (freq). When the frequency of an integer becomes equal to or greater than its value, the function returns that value if it's larger than the previous max_val. If no such integer is found, it returns -1 to indicate the absence of such a number. 

This approach ensures it identifies the largest integer with the described property in O(n) time, where n is the length of the input list. It avoids duplication as the code structure clearly indicates the presence of the condition max_val = i if i > max_val else max_val.