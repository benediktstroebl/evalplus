```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:len(array)//2+1:-1]
    else:
        return array[::-1]
```
This function relies on the observation that when an array is reversed and truncated, it will be sorted in ascending order. Conversely, if an array is reversed and not truncated, it will be sorted in descending order. The len(array) % 2 expression calculates whether the sum of the first and last index values is odd or even, determining whether the array should be reversed or not. Finally, the slicing notation is used to manipulate the array as necessary.