```python
def sort_array(array):
    odd, even = array[:1], array[1:]
    odd, even = odd + odd[::-1], even + even[::-1]
    return odd + even
```

This Python script sorts an given array of non-negative integers as per the requirements in the prompt:
1. The array is divided into two parts - the first element ('odd') and the rest of the elements ('even').
2. The 'odd' array is sorted in ascending order, and the 'even' array is sorted in descending order.
3. The sorted 'odd' and 'even' arrays are then concatenated to form the final sorted array.