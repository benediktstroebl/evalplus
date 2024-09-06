```python
def sort_array(array):
    odd, even = array[:1] + array[-1:], array[1:-1]
    return odd if sum(odd) % 2 else even
```

This code divides the array into two parts: `odd` and `even`. The `odd` array consists of the first element and the last element of the original array, while the `even` array contains everything in between. The function returns the `odd` array if the sum of the first and last elements is odd, and the `even` array if that sum is even. The result is a sorted version of the original array, based on the specified criteria.