```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script provides a function `sort_array` that accepts an array of non-negative integers as input. It aims to sort this array while respecting a specific sorting order based on the parity of the sum of the first and last elements of the array. If the sum is odd, the array is sorted in ascending order, and if the sum is even, it is sorted in descending order. This functionality is encapsulated within the `sorted` function, which is reversed when necessary to achieve the desired sorting order. Additionally, the function handles the edge case where the input array is empty, returning the original empty array as a result.