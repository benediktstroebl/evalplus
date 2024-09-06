```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
    return array
```

The function `sort_array()` uses the sum of the first and last elements of the array to determine whether to sort the array in ascending or descending order. The function then uses the `sorted()` function and depends on the `reverse` parameter to sort the array based on the odd or even sum. Additionally, the function uses the array-slicing notation `array[:] = sorted...` to update the original array instead of returning a new sorted array, as specified in the note in the prompt.