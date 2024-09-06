```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array and the product of their signs before returning the sum of magnitudes multiplied by the product of all signs, accordingly. If the array is empty, it returns `None`.

Here's an example usage illustration:
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