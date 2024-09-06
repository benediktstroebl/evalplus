```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script defines a function `sort_array` that takes an array of numbers as input. The function checks whether the length of the array modulo 2 is odd or even to determine whether to sort the array in ascending or descending order. Finally, it uses the `sorted` function with the `reverse` parameter set to `odd` to sort the array accordingly.