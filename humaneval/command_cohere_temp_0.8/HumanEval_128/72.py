```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the input array and determines its sign (1, -1, or 0). These values are then used to calculate the product of signs and the sum of magnitudes. Ultimately, the problem's requirement of multiplying these two outcomes is fulfilled. If the input array is empty, the function returns `None`.

Here's an example usage illustration:
```python
prod_signs([1, 2, 2, -4])  # Output: -9
prod_signs([0, 1])  # Output: 0
prod_signs([])  # Output: None
```
This exemplifies the function's behavior for various scenarios. The resulting value is aligned with the problem's stated expectation.