```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```

The function `sort_array()` uses the sum of the first and last elements of the array to determine whether to sort the array in ascending or descending order. If the sum is odd, it sorts the array in ascending order; otherwise, it sorts the array in descending order. Also, note that an empty array returns another empty array, as specified in the note of the problem.