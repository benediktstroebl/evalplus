```python
def sort_array(array):
    odd = len(array) % 2 != 0
    return sorted(array, reverse=odd)
```
This Python script defines a function `sort_array` that takes an array of integers as input. The function uses the modulo operator to check if the length of the array is odd or even. If the length is odd, the sorted array will be in ascending order, and if it's even, the sorted array will be in descending order. The `sorted` function with the `reverse` parameter sorts the array accordingly. The function returns a sorted copy of the input array based on the specified criteria.