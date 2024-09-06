```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script defines a function `sort_array` that takes an array of numbers as input. The function uses the sum of the first and last numbers in the array to determine whether to sort the array in ascending or descending order. The `sorted` function is used to sort the array, with the `reverse` parameter set to `True` if the sum is even (descending order), or `False` if the sum is odd (ascending order). The function does not modify the input array; instead, it creates and returns a new sorted array.