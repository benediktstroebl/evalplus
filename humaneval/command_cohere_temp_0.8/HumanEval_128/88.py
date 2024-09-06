```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the input array and identifies the sign of each number (1, -1, or 0), then returns the sum of the magnitudes multiplied by the product of all signs. If the input array is empty, it returns `None`.

Here's an example usage:
```python
prod_signs([1, 2, 2, -4]) # -9
prod_signs([0, 1]) # 0
prod_signs([]) # None
``` 
Which aligns with the examples provided in the initial problem description.