```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script defines a function `sort_array` that takes an array of non-negative integers as input. The function checks whether the length of the array modulo 2 is odd or even to determine whether to sort the array in ascending or descending order. The `sorted` function is used to sort the array based on this criteria and returns the sorted array.