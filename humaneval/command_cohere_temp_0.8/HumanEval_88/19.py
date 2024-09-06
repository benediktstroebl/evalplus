```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array, reverse=odd) if array else array
```

The code uses the sum of the first and last elements of the array to determine whether to sort in ascending or descending order. Ascending order is used if the sum is odd, and descending order is used if the sum is even. The sorted() function is used with the reverse parameter set to match the desired sort order.