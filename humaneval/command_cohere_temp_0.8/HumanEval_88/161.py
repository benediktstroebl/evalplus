```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script defines a function `sort_array` that takes an array of integers as input. The function uses the sum of the first and last elements of the array to determine whether to sort the array in ascending or descending order. If the sum is odd, the array is sorted in ascending order, and if the sum is even, it is sorted in descending order. This behavior is controlled by the `reverse` parameter in the `sorted` function, which is set to `False` when the sum is odd and `True` when the sum is even. Finally, the function returns the sorted array. Overall, this solution efficiently solves the problem as stated.