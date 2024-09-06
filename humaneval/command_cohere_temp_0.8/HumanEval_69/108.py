```python
def search(lst):
    freq, max_val = -1, 0 
    for i in lst:
        if i > 0:
            max_val = i if i > max_val else max_val 
            if i == max_val and lst.count(i) >= i:
                freq = i 
    return max_val if freq >= 0 else -1
```

The function iterates through the list of positive integers, maintaining the maximum value encountered (`max_val`) and its frequency (`freq`). When the frequency of an integer is greater than or equal to its own value, the function returns this value. If no such integer is found, it returns -1. This approach ensures that the function efficiently solves the problem in a single pass.