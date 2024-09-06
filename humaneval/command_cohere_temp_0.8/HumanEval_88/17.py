```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script sorts an array of non-negative integers, as specified by the problem statement. The function `sort_array` takes an array as input and returns a copy of the array sorted in the required manner. 

The sum of the first and last elements of the array is used to determine the sorting order: if the sum is odd, the array is sorted in ascending order, and if the sum is even, it is sorted in descending order. The `sorted` function is used with the `reverse` parameter set according to the sum value.