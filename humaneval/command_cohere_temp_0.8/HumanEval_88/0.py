```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        array = sorted(array)
    else:
        array = sorted(array, reverse=True)
    return array
```

This function uses the len(array) % 2 expression to determine whether the array should be sorted in ascending or descending order. Given that the sum of the first and last index values in the array is equal to the length of the array, we can utilize this property to determine whether the length is odd or even and consequently sort the array accordingly.

The function then uses the sorted() function to sort the array, passing in the optional reverse parameter set to True to sort the array in descending order. Finally, the function returns the sorted array.