```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting a list of objects. In this case, the lambda function `lambda x: (-bin(x).count('1'), x)` is used. It first counts the number of `1`s in the binary representation of the number `x` and sorts the list first according to this number, and in case of a tie, it sorts according to the decimal value of `x`. The function returns a sorted list according to the mentioned criteria. 

This approach leverages the built-in `sort` function to handle the sorting process, enhancing clarity and simplifying the overall implementation.