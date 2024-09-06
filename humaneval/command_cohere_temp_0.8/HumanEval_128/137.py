```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array using the `abs()` function and stores them in the `magnitudes` list. It then determines the signs of the integers using conditional statements and stores them in the `signs` list. Subsequently, it computes the sum of magnitudes and multiplies it by the product of signs, storing the result in the `result` variable.

The code includes a check to ensure that the input array is not empty. If the array is empty, the function returns `None`. 

The function returns the value of `result` resulting in the desired solution.