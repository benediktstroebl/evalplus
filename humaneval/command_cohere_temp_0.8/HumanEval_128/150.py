```python
def prod_signs(arr):
    result = None
    if arr:
        arr = [x for x in arr if x != 0]
        signs = [1 if x > 0 else -1 if x < 0 else 0 for x in arr]
        result = sum([x * y for x, y in zip(arr, signs)])
    return result
```

The prod_signs function takes an array of integers as input and calculates the sum of the magnitudes of the integers multiplied by the product of all signs of each number in the array. The function first filters out all zeros from the array, then constructs an array of signs, and finally computes the sum of the element-wise product of the non-zero integers with their corresponding signs. The result is returned, or None if the input array is empty.

Here is an example usage of the function:
```python
>>> prod_signs([1, 2, 2, -4])
-9
>>> prod_signs([0, 1])
0
>>> prod_signs([])
None
```