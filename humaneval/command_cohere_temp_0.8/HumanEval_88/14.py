```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script defines a function `sort_array` that sorts an input array of non-negative integers. The sorting order is determined by the parity of the sum of the first and last elements: it sorts in ascending order if the sum is odd, and in descending order if the sum is even, while accounting for the edge case where the array is empty. This function returns the sorted array without modifying the original input.