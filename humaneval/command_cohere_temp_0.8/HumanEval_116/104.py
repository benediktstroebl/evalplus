```python
def sort_array(arr):
    arr.sort(key=lambda x: (-bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that preprocesses the list elements before they are compared. In this case, the lambda function `lambda x: (-bin(x).count('1'), x)` first converts the list elements to strings and counts the number of ones in the binary representation. The number of ones is used for sorting in descending order and if there is a tie, it sorts the elements based on their decimal value in ascending order. The binary representation of the number is found using the `bin` string method. The result of the sorting is the sorted array that meets the specifications of the problem.