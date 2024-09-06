```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    if odd:
        array[:] = sorted(array)
    else:
        array[:] = sorted(array, reverse=True)
    return array
```

The function sorts the array as per the requirements: sorting in ascending order if the sum of the first and last elements is odd, and sorting in descending order if the sum is even. And, the `array[:]` line efficiently modifies the given array in-place, returning it after sorting. 

This solution has a time complexity of O(n log n) as it uses the `sorted` function.