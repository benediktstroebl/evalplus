```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
```

The `sort_array` function uses the len(array) % 2 formula to determine whether the array should be sorted in ascending or descending order. If the result is odd, it sorts the array in ascending order using sorted(array); otherwise, it sorts the array in descending order using sorted(array, reverse=True). The `:` notation is used to modify the original array.

This approach eliminates the need to define a new array and improves efficiency by modifying the original array directly. The compact code is easy to understand and achieves the desired result. It can be used as a building block for more complex sorting algorithms or analyzed as part of more advanced sorting paradigms.