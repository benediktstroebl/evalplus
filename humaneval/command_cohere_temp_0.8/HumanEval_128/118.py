```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(abs(x) for x in arr) * product(x%3 for x in arr)
    return result
```
This function employs Python's list comprehension and the `product()` function to calculate the product of signs and the sum of magnitudes respectively. Furthermore, it checks for input emptiness with an `if arr:` conditional and returns `None` when the input array is empty.