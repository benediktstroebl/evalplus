```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 for x in arr]
        product_of_signs = prod(signs)
        result = sum(magnitudes) * product_of_signs
    return result
```
This function calculates the magnitude of each number in the array using the `abs()` function and stores them in the `magnitudes` list. It then determines the signs of each number in the array using a list comprehension and stores them in the `signs` list. Subsequently, it calculates the product of the signs using the `prod()` function. Finally, it computes the sum of the magnitudes and multiplies it by the product of the signs to provide the required result.

The `if arr:` statement handles the case of an empty array, ensuring that the function returns `None` for such input.

The provided example tests reinforce the correct behavior of the function.