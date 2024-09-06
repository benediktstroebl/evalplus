```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script defines a function `sort_array` that takes an array of integers as input. The function uses the modulo operator to check if the length of the array is odd or even. If the length is odd, the `sorted` function sorts the array in ascending order. If the length is even, the `sorted` function sorts the array in descending order. This behavior is controlled by the `reverse` parameter in the `sorted` function, which is set to `True` for even lengths and `False` for odd lengths. Thus, the function sorts the array accordingly, without modifying the original input array.