```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```

The `sort_array` function uses the sum of the first and last elements of the array to determine whether to use ascending or descending sort order. The `sorted` function is used to sort the array, with the `reverse` parameter set to `True` if the sum is even, and to `False` otherwise. The base case handles the empty array, returning the array as is.