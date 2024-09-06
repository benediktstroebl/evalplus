```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script defines a function `sort_array` that takes an array of numbers as input. It checks whether the length of the array is odd or even to decide whether to sort the array in ascending or descending order. The `sorted` function is used to sort the array based on this decision. The result is a sorted array based on the decision made.