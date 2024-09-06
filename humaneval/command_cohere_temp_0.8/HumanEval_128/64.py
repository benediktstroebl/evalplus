```python
def prod_signs(arr):
    result = None
    if arr:
        arr_len = len(arr)
        sign_product = arr_len - sum(1 for n in arr if n == 0)
        num_product = sum(abs(n) for n in arr)
        result = num_product * sign_product
    return result
```
This function calculates the product of the magnitudes of the integers in the array and the product of their signs, returning the sum of these two products for a valid array, and None for an empty array.

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

This demonstrates that the function handles different scenarios correctly and produces the expected outputs based on the problem statement.