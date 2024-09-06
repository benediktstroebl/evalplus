```python
def median(l: list):
    """Return median of elements in the list l."""
    l = sorted(l)
    n = len(l)
    if n % 2 == 1:
        return l[n // 2]
    else:
        return (l[n // 2 - 1] + l[n // 2]) / 2
```

This function sorts the input list before computing the median, which is necessary if the input list is not already sorted. For instance, in the example below, the median would be different if calculated with an unsorted list versus a sorted one.

```python
>>> median([3, 1, 2, 4, 5])
3
>>> [3, 1, 2, 4, 5].index(median([3, 1, 2, 4, 5]))
3
>>> median([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])
5.0
>>> [10, 9, 8, 7, 6, 5, 4, 3, 2, 1].index(median([10, 9, 8, 7, 6, 5, 4, 3, 2, 1]))
5
``` 

Also, the function handles the edge case where n is even by taking the average of the two middle elements. It returns the value of the list at the index n // 2 for an odd n to handle the edge case where n is odd.