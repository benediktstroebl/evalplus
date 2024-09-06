```python
def median(lst):
    n = len(lst)
    if n % 2 == 0:
        return (lst[(n//2 - 1)] + lst[n//2]) / 2
    else:
        return lst[(n//2)]
```

This function calculates the median of the list. It handles the cases of even even or odd number of elements in the list. It works by taking the the middle two elements and calculating the average of them, ensuring the correct median value.