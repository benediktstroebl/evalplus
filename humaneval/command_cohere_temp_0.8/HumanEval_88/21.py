```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:len(array) // 2] + array[len(array) // 2:][::-1]
    else:
        return array[len(array) // 2:][::-1] + array[:len(array) // 2]
```

The function `sort_array()` takes an array of non-negative integers as input and returns a copy of the array sorted according to the specified rule. If the sum of the first and last indices of the array is odd, it sorts the array in ascending order. Otherwise, it sorts the array in descending order. This is done using slice assignments and reversing arrays.