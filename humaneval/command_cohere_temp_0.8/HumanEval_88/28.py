```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
```

The `sort_array()` function sorts the array in ascending order if the sum of the first and last indices of the array is odd, and sorts the array in descending order if the sum of the first and last indices is even. This behaviour is reflected in the `odd` variable which is set to `True` for odd sums and `False` for even sums, then used as a parameter in the `sorted()` function.