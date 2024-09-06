```python
def sort_array(arr):
    arr.sort(key=lambda x: (bin(x).count('1'), x))
    return arr
```

The `key` argument in the `sort` function is used to specify a function that returns the parameters for sorting. In this case, the function `lambda x: (bin(x).count('1'), x)` returns a tuple where the first element is the number of ones in the binary representation of the number, and the second element is the decimal value of the number. The `sort` function then sorts the array based on these parameters in ascending order. 

After sorting the array, the function returns the sorted array. 

This approach efficiently solves the task and results in a succinct and markdown-friendly solution. 

This code snippet should be added to the code block to complete the self-contained solution within the provided markdown code block.