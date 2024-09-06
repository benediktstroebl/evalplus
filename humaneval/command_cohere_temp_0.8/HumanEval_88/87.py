```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:] if array == [] else sorted(array)
    return sorted(array, reverse=True) if array != [] else array
```
This Python script provides a function `sort_array` that takes an array of non-negative integers as input. The function copies the input array without modification if it's empty; this is consistent with the given example cases. If the input array is not empty, the function sorts the array in ascending order if the length of the array is odd, and in descending order if the length is even. The `odd` variable calculates the parity of the array length using the modulus operator, simplifying the condition checks. The function uses the built-in `sorted` function to sort the array according to the specified order and returns the sorted array.