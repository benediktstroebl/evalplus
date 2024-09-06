```python
def median(l):
    # Sort the list
    l.sort(l)
    # Get the length of the list
    n = len(l)
    # If the list has an odd length, return the middle element
    if n % 2 == 1:
        return l[n // 2]
    # If the list has an even length, return the mean of the two middle elements
    else:
        return (l[n // 2 - 1] + l[n // 2]) / 2
```
This Python function, `median`, takes a list `l` as input and calculates the median of its elements. The function sorts the process a list using the `sort()` function and then determines whether the list has an odd or even length. 

Depending on this condition, the function returns either the middle element of the list or the average of the two middle elements. The code is self-contained and can be easily adapted for different lists.