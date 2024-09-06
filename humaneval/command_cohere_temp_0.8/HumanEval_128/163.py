```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the array using the `abs()` function and stores them in the `magnitudes` list. It then determines the sign of each number in the array and stores them in the `signs` list. Subsequently, it returns the sum of the magnitudes multiplied by the product of all signs, represented by 1, -1, or 0, coercing the product to be float as needed by the `prod()` function.

The `if arr:` statement is used to check if the input array is not empty, and therefore decides whether to proceed with the calculations or return `None`. 

The function returns `None` for an empty input array, and the specified test cases illustrate its usage and correctness. 
```python
prod_signs([1, 2, 2, -4]) == -9
prod_signs([0, 1]) == 0
prod_signs([]) == None
```