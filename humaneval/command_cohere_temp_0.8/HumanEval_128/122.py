```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the array using the `abs()` function and stores them in the `magnitudes` list. It then determines the sign of each number in the array using conditional statements and stores them in the `signs` list. These computations allow the function to compute the desired result. 
The `result` variable is initialized as `None` to handle the case when the array is empty, and the result is assigned to it only when the array is not empty. In the returned result, the sum of magnitudes is multiplied by the product of all signs of each number in the array. This is achieved using the `prod()` function that calculates the product of all elements in the `signs` list. 

The function checks for an empty array and returns `None` when appropriate, as specified in the problem statement. 

This solution effectively solves the problem using basic Python algorithms and constructs.