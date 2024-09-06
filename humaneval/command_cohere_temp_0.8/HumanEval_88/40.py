```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array if odd else reversed(array)) if array else array
```

The code uses `sum(array[0], array[-1])` to get the sum of the first and last elements of the array, and then uses `% 2` to check if the sum is even or odd to decide whether to sort the array in ascending or descending order using `sorted(reversed(array))`. The special case of an empty array is handled as well since `sorted()` and `reversed()` return empty lists for empty inputs.