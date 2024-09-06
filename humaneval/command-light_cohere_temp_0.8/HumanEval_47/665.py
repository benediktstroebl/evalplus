```python
def median(lst):
    n = len(lst)
    if n <= 1:
        return float('-inf')  # handle empty list or single element list
    mid = n // 2
    if lst[mid] > lst[n - mid]:
        mid += 1
    return (len(lst) + 1) * (lst[mid] + lst[n - mid]) / 2
```
The function median takes a list as an argument and returns the median value of the list's elements. It handles cases where the fact the median of a list is calculated by finding the middle value(s) and the value of the list at the extreme ends, and then averaging them. 

Feel free to test the code with different input lists!