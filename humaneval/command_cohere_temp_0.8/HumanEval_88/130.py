```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script provides a function `sort_array` that sorts an array of non-negative integers. The sorting order is determined by the parity of the length of the array: if the length is odd, it sorts in ascending order, and if the length is even, it sorts in descending order. This behavior is dictated by the line `return sorted(array, reverse=odd)`, where `sorted` is used with the `reverse` parameter set to `odd`, which sorts the array in reverse order if odd is `True` and in the usual order if odd is `False.`