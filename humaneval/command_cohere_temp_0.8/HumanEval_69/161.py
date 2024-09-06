```python
def search(lst):
    freq, max_val = -1, 0
    for n in lst:
        if n > 0:
            max_val = max(max_val, n)
            freq = lst.count(n)
            if freq >= n: return n
    return -1
```
The function iterates through the list, tracking the maximum value in the list (`max_val`) and its corresponding frequency (`freq`). When the frequency of a number is greater than or equal to the number itself, the function returns this number. If no such number is found, it returns -1. This approach is efficient due to its linear time complexity (`O(n)`), as it iterates the list only once.