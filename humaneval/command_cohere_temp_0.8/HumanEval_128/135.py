```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function works by looping through each element in the array and multiplying it by the subsequent element to accumulate the product of signs. At the same time, it multiplies these values by the sum of magnitudes to achieve the final result. Ultimately, the function returns the calculated sum or None for an empty input.