```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitude of each number in the array using the `abs()` function and stores them in the `magnitudes` list. It then determines the signs of each number in the array and stores them in the `signs` list. Finally, it returns the sum of the magnitudes multiplied by the product of all signs, represented by 1, -1, or 0, opting for `None` when the array is empty.

Here's an example usage of the function:
```python
prod_signs([1, 2, 2, -4]) # -9
prod_signs([0, 1]) # 0
prod_signs([]) # None
``` 
And here's the corresponding Markdown code block:
```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
``` 

This code block represents a Python function named `prod_signs`, designed to compute the product of the magnitudes and signs of an array of integers. The function initially checks if the input array is empty; if so, it returns `None`. Otherwise, it proceeds by calculating the magnitude of each number using the `abs()` function and storing them in the `magnitudes` list. Simultaneously, it determines the sign of each number (1 for positive, -1 for negative, and 0 for zero) and stores them in the `signs` list. Finally, the function returns the sum of the magnitudes multiplied by the product of all signs, ensuring correct handling of positive, negative, and zero values.