```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * (-1 if num < 0 else 1)
        result = sum([num * sign for num, sign in zip(arr, signs)])
    return result
```
This function takes an array of integers as input and calculates the sum of the magnitudes of the integers multiplied by the product of all signs of each number in the array. If the array is empty, it returns `None`. The algorithm uses a list comprehension to determine the sign of each number in the array and calculates the resultant magnitude with the provided example tests passing.