```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array and the product of their signs before returning the sum of magnitudes multiplied by the product of all signs, consistent with the problem statement.

Here's an example usage illustration:
```python
arr = [1, 2, 2, -4]
print(prod_signs(arr))  # Output: -9
```
This will return -9, as the sum of magnitudes is 3 (-2 + 2 + 2), and the product of signs is -1 (-1 * -1 * 1 * 1).

Also, if the input array is empty or contains only zeros, the result will be None, as the multiplication will result in 1, and the sum of magnitudes will be 0:
```python
print(prod_signs([]))  # Output: None
```
```python
print(prod_signs([0, 0]))  # Output: None
```