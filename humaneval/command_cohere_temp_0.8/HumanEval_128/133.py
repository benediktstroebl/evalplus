```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array and the product of their signs, then returns their sum multiplied together. If the array is empty, it returns `None`.

Here is an example usage of the function:
```python
prod_signs([1, 2, 2, -4]) # -9
prod_signs([0, 1]) # 0
prod_signs([]) # None
``` 
This would output:
- `-9`
- `0`
- `None` 
respectively, corresponding to the examples provided in the problem statement. 

This effectively solves the problem as required.