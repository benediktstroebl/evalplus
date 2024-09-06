```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script sorts an array of non-negative integers based on the sum of its first and last elements, it uses the sum modulus 2 to determine whether to sort in ascending or descending order, and then employs the `sorted` function with the `reverse` parameter set accordingly. If the input array is empty, it's returned as-is. This ensures the integrity of the original array while delivering the required sorted result.