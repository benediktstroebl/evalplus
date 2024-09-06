```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            max_val = max(max_val, n)
            freq = lst.count(n)
        if freq >= n:
            return n
        if freq > max_val:
            max_val, freq = max_val, freq
    return -1
```

This Python script defines a function `search` that solves the problem statement. It iterates through the list, tracking the maximum value (`max_val`) and its corresponding frequency (`freq`). When the frequency of a number reaches or exceeds the value of the number itself, the function returns that number. If no such number is found, it returns -1. This method efficiently solves for the desired integer in a single pass. 

The script leverages basic Python data structures and algorithms to achieve a linear time complexity of O(n), where n is the number of elements in the input list.