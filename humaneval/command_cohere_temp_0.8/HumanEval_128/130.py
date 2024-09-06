```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * (-1 if num < 0 else 1)
        result = sum([num * sign for num, sign in zip(arr, signs)])
    return result
```
This function utilizes Python's ability to assign boolean values to lists, leveraging it to calculate the product of signs for each number in the input array. Subsequently, it calculates the sum of the magnitudes multiplied by the product of signs. If the input array is empty, the function returns `None`.

Here is a markdown code block showcasing how to utilize the function with test cases:
```python
# Test Cases
assert prod_signs([1, 2, 2, -4]) == -9
assert prod_signs([0, 1]) == 0
assert prod_signs([]) == None
```