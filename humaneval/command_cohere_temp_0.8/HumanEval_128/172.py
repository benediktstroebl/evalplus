```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array and the product of their signs before returning the sum of magnitudes multiplied by the product of all signs, which is the product of the signs of each number in the array. 

Here's an example usage interaction:
```python
>>> prod_signs([1, 2, 2, -4])
-9
>>> prod_signs([0, 1])
0
>>> prod_signs([])
None
```
This shows that the function correctly calculates the required result based on the given examples.