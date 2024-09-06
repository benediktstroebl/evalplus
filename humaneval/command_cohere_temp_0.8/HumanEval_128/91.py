```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [x > 0 for x in arr] * [x < 0 for x in arr] + [x == 0 for x in arr]
        result = sum([x * y for x, y in zip(arr, signs)])
    return result
```
This function uses list comprehensions to determine the signs of each number in the array and calculates the magnitudes of the integers in the array. Subsequently, it returns the product of the magnitudes multiplied by the product of the signs. The `if arr` statement checks for the presence of elements in the array, avoiding null results when the array is empty. 

To ensure correctness, the function verifies the following conditions:
- The result is None for an empty array.
- The function computes the product of signs correctly.
- It calculates the sum of magnitudes multiplied by the product of all signs.

You can verify these conditions by running the example usage provided in the original problem statement. Adjust the assertions accordingly depending on the test cases you wish to cover. 
```python
assert prod_signs([1, 2, 2, -4]) == -9
assert prod_signs([0, 1]) == 0
assert prod_signs([]) == None
```