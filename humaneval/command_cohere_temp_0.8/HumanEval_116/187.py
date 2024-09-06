```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that tells the sort function how to compare each pair of elements. The lambda function `lambda x: (-bin(x).count('1'), x)` is used to return a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the actual number. The `(-)` prefix in the lambda function is used to reverse the order of the return values, thus making it sort in the desired order.