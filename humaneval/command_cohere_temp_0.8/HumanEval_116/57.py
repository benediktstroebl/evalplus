```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before comparison. Here, it handles the binary representation of the numbers to sort them first by the number of `1` digits and then, in the case of a tie, by their numerical value. 

The resulting sorted list is returned.