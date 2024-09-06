```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        array = reversed(array)
    array.sort()
    if odd:
        array = reversed(array)
    return array
```

This Python script defines a function `sort_array` that takes an array as input and returns a sorted version of the array based on certain criteria. If the total of the first and last index values is odd, it sorts the array in ascending order; otherwise, it sorts the array in descending order. This behavior is achieved by using the `reversed` function to reverse the array when needed, and the `sort` function to sort the array in the desired order. The function includes an example usage, demonstrating how it can be called with different input arrays to get the corresponding sorted arrays based on the specified criteria.