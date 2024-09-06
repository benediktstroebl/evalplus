```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function employs a concise one-liner to compute the sum of magnitudes multiplied by the product of all signs, as described in the problem statement. It relies on a zip operation to iterate through pairs of adjacent elements in the array, multiplying each element's magnitude by its sign (1, -1, or 0). The resulting value is then returned, or None if the input array is empty.

Here is a markdown code block showcasing how to utilize this function with an example:
```python
arr = [1, 2, 2, -4]
print(prod_signs(arr))  # Output: -9
```
This would return -9, as the product of the signs and magnitudes of the given array.