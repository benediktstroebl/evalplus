```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that formats the element as a binary string and counts the number of ones, sorting in descending order. The element is then sorted according to this value, as specified in the problem statement.