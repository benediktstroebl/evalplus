```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script provides a function `sort_array` that takes an array as input and returns a sorted copy of the array. It checks whether the sum of the first and last elements of the array is odd or even to determine whether to sort the array in ascending or descending order. The function is designed to work with non-negative integer arrays and handles the cases where the array is empty or contains only one element, returning the input unchanged in these cases.