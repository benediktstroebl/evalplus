```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(abs(num) for num in arr) * product(sign(num) for num in arr)
    return result

def sign(num):
    if num > 0:
        return 1
    elif num < 0:
        return -1
    else:
        return 0
```
The `prod_signs` function takes an array of integers as input and calculates the requested product of signs and magnitudes. If the input array is empty, it returns `None`. The `sign` helper function determines the sign of each number in the array, returning 1 for positive numbers, -1 for negative numbers, and 0 for zero. The result is then multiplied by the sum of magnitudes of the integers in the array, resulting in the desired outcome.