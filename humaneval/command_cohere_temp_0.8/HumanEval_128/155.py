```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(abs(x) for x in arr) * product(x % 2 for x in arr)
    return result
```
The `prod_signs` function takes an array `arr` as input and returns the sum of magnitudes of integers multiplied by the product of all signs of each number in the array. The function checks if the array is empty, and returns `None` if so. Otherwise, it uses two generators to extract the magnitude and sign of each number, respectively, and multiplies them together to return the result. 

You can use the function by calling it and passing an array of integers as an example as shown in the comments in the code block above. You can also use the function by calling it and passing an array of integers as argument as needed.