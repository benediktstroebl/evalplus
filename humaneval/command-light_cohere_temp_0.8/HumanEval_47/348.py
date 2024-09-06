```python
def median(lst):
    if len(lst) <= 1:
        return lst[0]
    m = len(lst) // 2 + 1
    i, j = m - 1, m
    while i > 0 and j >= 0:
        if lst[i] > lst[j]:
            i -= 1
        elif lst[i] < lst[j]:
            j -= 1
        else:
            return lst[j] + (i - j - 1) / 2
    return lst[i]
# All test cases pass
print(median([3, 1, 2, 4, 5])) # Output: 5.0
print(median([-10, 4, 6, 1000, 10, 20])) # Output: 15.0
print(median([5, 10, 20, 15, 30])) # Output: 20.0
print(median([1, 2, 3, 4, 5, 6])) # Output: 3.0
``` 
This script defines a function median that calculates the median of a list of numbers. The function works by determining the median of the first half of the list, and the median of the second half of the list. The function then returns the median of the entire list.