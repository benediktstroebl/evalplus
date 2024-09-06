```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of the integers in the array and multiplies them with the product of all signs of each number in the array. The result is returned if the array is not empty, and `None` is returned otherwise.

Here's an example usage illustration:
```python
prod_signs([1, 2, 2, -4])  # Output: -9
prod_signs([0, 1])  # Output: 0
prod_signs([])  # Output: None
```
You can readily incorporate this Python script within a markdown code block to fulfill the problem statement.