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
The code uses Python's list comprehension and prod function to calculate the required values. The result is then calculated using the provided formula and returned. Note that the function returns None for an empty list to comply with the problem's requirement.