```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that formats the elements of the list before they are compared. In this case, each element `x` is converted to its binary representation using the `bin` function. The resulting string `bin(x)` contains a binary representation of the element, where '1' represents a binary digit that is `1` and `0` represents a binary digit that is `0`. The `count` method is used to count the number of occurrences of '1' in the binary representation. This count is used to sort the elements in ascending order. If the count is the same for two elements, they are sorted by their decimal value, as specified in the prompt.