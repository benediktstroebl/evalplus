```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array if odd else reversed(array)) if array else array
```

The function `sort_array()` sorts the array based on the sum of its first and last elements, odd sums sort the array in ascending order, and even sums sort the array in descending order. The function returns a sorted array or the original unsorted array if empty. 

This solution utilizes Python's built-in `sorted()` and `sum()` functions to efficiently sort the array, and the `if array else array` condition handles the case of an empty array, returning empty in that case as well.