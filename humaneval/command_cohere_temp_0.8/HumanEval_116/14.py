```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` method is used to specify a function that sorts the array based on the returned values. In this case, for each element in the array, the lambda function `lambda x: (bin(x).count('1'), x)` is used. This function first counts the number of occurrences of '1' in the binary representation of the element `x` and then returns this count along with the element value `x`. The array is then sorted based on these returned values.

The code implements the specifications of the problem and produces the expected output. It is concise and efficient, making it a good illustration of a good solution to this kata. You can test the code by calling the `sort_array` function with the example input arrays provided in the problem statement.