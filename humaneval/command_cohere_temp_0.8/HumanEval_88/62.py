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
This Python script defines a function `sort_array` that takes an array as input. The function checks whether the length of the array is odd using the modulo operator. If the length is odd, it reverses the array using the `reversed` function, sorts it in ascending order using the `sort` function, and then reverses it again to restore the original order. If the length is even, it directly sorts the array in ascending order. In both cases, the function returns the sorted array without modifying the original input.