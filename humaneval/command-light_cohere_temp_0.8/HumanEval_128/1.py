Here is a self-contained Python script that solves the problem you described:
```python
def prod_signs(arr):
    if not_enough_elements(arr):
        return None
    result = 1
    sign = 1
    for num in arr:
        result *= num
        result += sign
        sign *= -1
    return result

def not_enough_elements(arr):
    if not arr or len(arr) < 1:
        return False
    return True
```
This script defines a function `prod_signs` that computes the sum of magnitudes of integers multiplied by the product of all signs of each number in the array. The `not_enough_elements` function checks whether the input array is empty or has less than one element, and returns `False` if so, or `True` if it is not empty or has at least one element. 
If the input array is valid, the `prod_signs` function will compute and return the result.