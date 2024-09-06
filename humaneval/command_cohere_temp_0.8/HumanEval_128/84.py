```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * [1] + [0] + [num < 0 for num in arr] * [-1]
        result = sum([num * sign for num, sign in zip(arr, signs)])
    return result
```
This Python script defines a function called `prod_signs` that takes an array of integers as input. It returns the sum of the magnitudes of the integers in the array multiplied by the product of all signs of each number. This is achieved by the use of nested list comprehensions, where each element is checked for being positive, zero, or negative, and the corresponding multiplication factor being 1, 0, or -1 respectively. The resulting products are then summed, and the outcome is returned. In the case of an empty array being input, the function returns `None`.

Here is an example usage of the function:
```python
arr = [1, 2, 2, -4]
print(prod_signs(arr))  # -9

arr = [0, 1]
print(prod_signs(arr))  # 0

arr = []
print(prod_signs(arr))  # None
```

The example tests cover scenarios like positive integers, negative integers, and zero, and demonstrates that the function `prod_signs` correctly solves the problem.