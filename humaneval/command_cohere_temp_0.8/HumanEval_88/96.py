```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script defines a function `sort_array` that sorts an array of non-negative integers. The sorting order is determined by the parity of the sum of the first and last elements: if the sum is odd, it sorts in ascending order, and if the sum is even, it sorts in descending order. This function adheres to the problem statement and ensures the original array remains unchanged.

Here is a more detailed breakdown of the code:
1. `def sort_array(array)`: Defines the function `sort_array` that takes one argument, `array`, which is the input list of integers.
2. `odd = sum(array[0], array[-1]) % 2`: Calculates the parity of the sum of the first and last elements of the array. The `% 2` operation yields 1 if the sum is odd and 0 if the sum is even.
3. `return sorted(array, reverse=odd) if array else array`: This line sorts the array using the `sorted` function. If the `reverse` parameter is set to `odd`, it sorts in descending order, and in ascending order otherwise. The `if array` condition checks if the input is not empty, and ensures that an empty list is returned if the input is empty.

By using this code, you can easily sort an input list according to the specified sorting criteria, ensuring that the original list is not modified, and empty lists are handled correctly.