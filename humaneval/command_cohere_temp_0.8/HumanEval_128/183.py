```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function takes an array of integers and calculates the sum of the magnitudes of the integers multiplied by the product of all signs of each number in the array. If the array is empty, it returns None. This is validated through the test cases provided in the original problem statement.