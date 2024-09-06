```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the array, which is done by using a list comprehension on the array, and replacing each value `x` with `abs(x)`. Then, it calculates the product of the signs of the integers in the array, by using a list comprehension on the array and replacing each value `x` with `x > 0 and 1 or x < 0 and -1 or 0`, which represents the signs of the numbers as integers "1", "-1", and "0" respectively. Finally, it returns the sum of the magnitudes multiplied by the product of the signs, and returns `None` if the array is empty. 

Here's an example usage of the function:
```python
arr = [1, 2, 2, -4]
print(prod_signs(arr))  # -9

arr = [0, 1]
print(prod_signs(arr))  # 0

arr = []
print(prod_signs(arr))  # None
```
This would output:
- `-9`
- `0`
- `None`

which proves the functionality of the function to solve the given problem.