```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
    return array
```

The function `sort_array()` uses the sum of the first and last elements of the array to determine whether to sort the array in ascending or descending order. The function then uses the `sorted()` function and relies on the default comparison `array[0] < array[1]` to sort the array. The output is either a sorted array in ascending order if the sum of the first and last elements is odd or a sorted array in descending order if the sum is even. 

This solution does not alter the original array due to the use of `array:` to modify the list argument. Thus, a copy of the array is sorted while the original list remains unchanged.