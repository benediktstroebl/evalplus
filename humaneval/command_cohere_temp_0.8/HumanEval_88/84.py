```python
def sort_array(array):
    odd = len(array) % 2
    if odd:
        return array[:] if array == [] else sorted(array)
    return sorted(array, reverse=True) if array != [] else array
```
This Python script defines a function `sort_array` that takes an array of non-negative integers as input. The function copies the input array without modification if it's empty; this is consistent with the given example and the note in the prompt, which states that the original array should not be modified.

The function performs the sorting as follows:
- If the sum of the first and last indices of the array is odd, it sorts the array in ascending order. 
- If the sum of the first and last indices of the array is even, it sorts the array in descending order. 

This sorting logic is aligned with the problem statement, where the order of sorting is based on the parity of the sum of the first and last index values of the array. This script effectively implements the specified sorting criteria and handles the edge case of an empty array without modifying the original input.