```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script provides a function `sort_array` that takes an array as input and returns a sorted copy of the array. The sorting order is determined based on the parity of the sum of the first and last elements of the array. If the sum is odd, the array is sorted in ascending order; if the sum is even, it is sorted in descending order. This approach utilizes Python's built-in `sorted` function and expresses the sorting criteria in a concise and clear manner.