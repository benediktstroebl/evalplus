```python
def sort_array(array):
    odd, even = sorted(array), sorted(array, reverse=True)
    return odd if sum(array[0], array[-1]) % 2 else even
```

The script uses basic conditional logic to sort the array differently based on whether the sum of the first and last items is odd or even. This logic is then applied based on the parity of that sum. This solution efficiently sorts the array according to the specified criteria without modifying the original input array.