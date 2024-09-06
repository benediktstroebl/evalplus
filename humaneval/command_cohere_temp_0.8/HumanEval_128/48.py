```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function follows the specification closely. If the input array `arr` is empty, it returns `None`. If `arr` contains integers, it calculates the sum of their magnitudes and the product of their signs separately and then multiplies these two quantities together to return the desired result. This approach ensures that the function handles all the edge cases mentioned in the specification.

Here is an example usage illustration:
```python
prod_signs([1, 2, 2, -4])  # Output: -9
prod_signs([0, 1])  # Output: 0
prod_signs([])  # Output: None
```
This demonstrates the function's behavior for the examples provided in the specification.