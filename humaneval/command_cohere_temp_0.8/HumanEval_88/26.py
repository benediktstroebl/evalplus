```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script defines a function `sort_array` that sorts the array based on the parity of the length of the array. If the length is odd, it sorts the array in ascending order; otherwise, it sorts the array in descending order. This behavior is controlled using the `reverse` parameter in the `sorted` function.