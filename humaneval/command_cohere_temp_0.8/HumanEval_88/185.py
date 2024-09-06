```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script provides a function `sort_array` that sorts an array of non-negative integers. The sorting order is determined by the parity of the length of the array: if the length is odd, it sorts in ascending order, and if the length is even, it sorts in descending order. This behavior is controlled by the `reverse` parameter in the `sorted` function, which is set to `True` for descending order when the length is even and to `False` for ascending order when the length is odd. Thus, the function efficiently sorts the array according to the given criteria without mutating the original input.