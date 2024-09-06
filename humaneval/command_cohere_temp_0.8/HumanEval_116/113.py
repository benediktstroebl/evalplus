```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before comparison. Here, it handles the binary representation of the numbers and their decimal value, if there is no difference in the number of ones. 

You can test this function by adding the corresponding tests provided in the problem statement to ensure it behaves as expected.