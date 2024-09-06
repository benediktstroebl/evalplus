```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that takes an element and returns a key to sort by. In this case, each element `x` is converted to a string `bin(x)` representing its binary representation, and the count of ones in that representation is counted using `count('1')`. If the count is the same for two elements, they are compared by their decimal value as specified in the prompt.