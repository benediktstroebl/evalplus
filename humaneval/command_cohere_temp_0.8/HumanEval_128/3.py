```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the array, then calculates the product of the signs of the integers in the array, and finally returns the sum of the magnitudes multiplied by the product of the signs. The `prod` function is used to calculate the product of a list of values, returning 1 if an empty list is passed.

Here is an example usage of the function:
```python
arr1 = [1, 2, 2, -4]
print(prod_signs(arr1))  # -9

arr2 = [0, 1]
print(prod_signs(arr2))  # 0

arr3 = []
print(prod_signs(arr3))  # None
``` 

This would output:
```
-9
0
None
```

This method utilizes the iterable `prod` function to compute the product of the signs array, providing a concise and efficient solution.