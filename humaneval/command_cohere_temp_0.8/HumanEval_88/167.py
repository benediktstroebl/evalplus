```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script defines a function `sort_array` that takes an array of non-negative integers as input. The function checks whether the length of the array is odd or even to determine whether the array should be sorted in ascending or descending order. Then, it uses the `sorted` function to sort the array based on this criteria and returns the sorted array.