```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the input array and combines them with the product of all signs of each number, returning the result as stated in the problem description. If the input array is empty, it returns `None`.

Here's an example usage:
```python
prod_signs([1, 2, 2, -4]) # Output: -9
prod_signs([0, 1]) # Output: 0
prod_signs([]) # Output: None
``` 
This illustrates how the function correctly handles different scenarios.