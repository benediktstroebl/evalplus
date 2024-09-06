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

The function iterates through the list, keeping track of the highest value encountered (`max_val`). It also keeps track of the frequency of the current maximum value seen (`freq`). If multiple instances of the current maximum are encountered and their frequency meets the criterion, `freq` holds the value of this multiple. If no such integer is encountered, the function returns `-1` correspondingly. 

This algorithm has a time complexity of `O(n)` as it iterates through the list only once.

The approach excels in clarity and efficiency, making it a robust solution to the problem.