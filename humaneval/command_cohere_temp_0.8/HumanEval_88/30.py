```python
def sort_array(array):
    odd = sum(array[0], array[-1]) % 2
    return sorted(array if odd else reversed(array)) if array else array
```

The function 'sort_array' sorts the array based on the sum of the first and last elements, which determines whether it should be sorted in ascending or descending order. If the sum is odd, it sorts the array normally; if it's even, it sorts the array in reverse. The result is then returned as a new array without altering the original input.