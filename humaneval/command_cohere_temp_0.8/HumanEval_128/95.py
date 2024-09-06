```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the array and multiplies them by the product of all signs of each number in the array. The result is None if the array is empty.

Here is an example usage of the function:
```python
arr = [1, 2, 2, -4]
print(prod_signs(arr))  # -9

arr = [0, 1]
print(prod_signs(arr))  # 0

arr = []
print(prod_signs(arr))  # None
```
This would output:
```
-9
0
None
```

This Python script defines a function `prod_signs` that solves the problem as stated in the markdown code block. It calculates the magnitude of each number in the input array and then finds the product of the signs of each number. The magnitudes are multiplied by this product of signs to get the final result. The function returns `None` for an empty input array.