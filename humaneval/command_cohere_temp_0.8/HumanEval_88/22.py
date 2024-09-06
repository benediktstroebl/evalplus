```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
    return array
```

The function `sort_array()` uses the sum of the first and last elements of the array to determine whether to sort the array in ascending or descending order. The function then uses the `sorted()` function and relies on the default comparison behavior to sort the array accordingly. Note that the modification of the `array` parameter uses the slice notation `array[:]`, which creates a copy of the array rather than modifying the original array. This is a more robust solution than the previous approach that used `sort` directly, which doesn't create a copy of the list and thus wouldn't pass the given test cases correctly.