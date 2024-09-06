```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```
This Python script sorts an array of non-negative integers based on the sum of its first and last elements. If the sum is odd, it sorts the array in ascending order, and if the sum is even, it sorts in descending order. The function uses the sum and modulus operations to determine the desired sort order and the sorted() function to rearrange the elements accordingly. As the problem suggests, the function returns a copy of the sorted array, ensuring the original array remains unmodified.