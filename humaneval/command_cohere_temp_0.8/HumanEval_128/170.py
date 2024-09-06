```python
def prod_signs(arr):
    result = None
    if arr:
        arr_signs = [num // abs(num) for num in arr]
        result = sum(num * sign for num, sign in zip(arr, arr_signs) if sign)
    return result
```

The function `prod_signs()` takes an array (`arr`) as input and returns the sum of magnitudes of integers multiplied by the product of all signs of each number in the array. If the array is empty, it returns `None`.

The script assumes that the given array contains only integers and raises a `TypeError` if it contains any non-integer value. You can add additional checks to handle non-integer inputs as needed.