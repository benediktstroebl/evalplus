```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that transforms each element in the list before comparison. Here, the lambda function `lambda x: (bin(x).count('1'), x)` first calculates the number of `1`s in the binary representation of each element `x` using the `bin` function, and then counts these `1`s using the `count` method. The resulting tuple `(count_ones(x), x)` is used to sort the array first based on the number of `1`s in the binary representation in ascending order, and then, for elements with similar number of `1`s, by their decimal value in ascending order. 

This approach ensures that the output of the function satisfies the given tests.