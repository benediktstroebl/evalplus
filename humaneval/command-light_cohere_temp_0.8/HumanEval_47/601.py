```python
def median(l):
    # Sort the list
    l.sort(l)
    # Get length of the list
    n = len(l)
    # Calculate middle index
    m = n // 2
    # Calculate the median
    median = l[m] if n % 2 == 0 else (l[m - 1] + l[m]) / 2
    return median
``` 
This Python function, `median()`, takes a list `l` as input and solves the problem of finding the median of its elements. It first sorts the By default, the list in ascending order using the `sort` method. It then gets thering length of the list `n` using the `len` function. 

Next, the function calculates the middle index `m` of the sorted list, which represents the position of the median element. If the length of the list is even, `n` is even, and the median is the middle element, `l[m]`. If the length of the list is odd, the median is the average of the two middle elements, calculated as `l[m - 1] + l[m]`. The function then returns the calculated median.