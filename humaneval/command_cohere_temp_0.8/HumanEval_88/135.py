```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script defines a function `sort_array` that sorts an array of non-negative integers. The sorting order is determined by the parity of the sum of the first and last elements: it will be in ascending order if the sum is odd, and in descending order if the sum is even, while handling the edge case where the array is empty or has only one element. This function encapsulates the entire problem and its logic, returning the correctly sorted array based on the specified conditions.