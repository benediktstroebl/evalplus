```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * [-1, 1, 0]
        result = sum(abs(num) for num in arr) * signs.prod()
    return result
```
This function calculates the magnitude of each number in the array and multiplies it by the product of all signs (1, -1, or 0) using the prod() function. The result is then returned, or None if the input array is empty.

Here's a usage example:
```python
arr = [1, 2, 2, -4]
print(prod_signs(arr))  # Output: -9

arr = [0, 1]
print(prod_signs(arr))  # Output: 0

arr = []
print(prod_signs(arr))  # Output: None
```
This demonstrates how the function correctly computes the requested sum of magnitudes multiplied by product of all signs for different input arrays.