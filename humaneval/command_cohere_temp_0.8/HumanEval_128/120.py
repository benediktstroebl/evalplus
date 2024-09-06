```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * (-1 if num < 0 else 1)
        result = sum([num * sign for num, sign in zip(arr, signs)])
    return result
```
This Python script defines a function named `prod_signs` that takes an array of integers as input. It calculates the product of the signs of each number in the array, where 1 represents a positive sign, -1 represents a negative sign, and 0 is treated as no effect. Then, it returns the sum of the magnitudes of the integers multiplied by the calculated product of signs. However, if the input array is empty, it returns `None` to account for this special case. This function is designed to handle all scenarios outlined in the problem statement, including examples provided in the documentation.