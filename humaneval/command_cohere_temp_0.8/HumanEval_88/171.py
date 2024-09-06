```python
def sort_array(array):
    odd, even = False, False
    if sum(array[0], array[-1]) % 2 == 1:
        odd = True
    if sum(array[0], array[-1]) % 2 == 0:
        even = True
    if odd:
        array[:] = sorted(array, reverse=False)
    if even:
        array[:] = sorted(array, reverse=True)
    return array
```

The function `sort_array()` takes an array of integers as input. It checks the parity of the sum of the first and last elements of the array. If the sum is odd, it sorts the array in ascending order using the `sorted()` function with `reverse=False`. If the sum is even, it sorts the array in descending order using the `sorted()` function with `reverse=True`. Ultimately it returns the sorted array.