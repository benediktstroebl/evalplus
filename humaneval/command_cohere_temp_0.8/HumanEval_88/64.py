```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
```

This Python script provides a function `sort_array` that takes an input array and sorts it in the specified manner. The sum of the first and last elements of the array is used to determine whether it should be sorted in ascending or descending order. This function complies with the problem statement's requirement that the input array be changed in place, as shown in the provided examples.