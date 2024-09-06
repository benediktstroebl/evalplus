```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the array and multiplies them with the product of all signs of each number in the array. The result is returned if the array is not empty, otherwise `None` is returned. 
To test this function, you can call it with the examples provided in the original problem statement.