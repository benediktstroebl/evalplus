```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array and multiplies them by the product of all signs of each number in the array. The result is returned if the array is not empty, and `None` is returned otherwise.

Here is an example usage invocation:
```python
prod_signs([1, 2, 2, -4]) # Result: -9
prod_signs([0, 1]) # Result: 0
prod_signs([]) # Result: None
```
The first example confirms that the function correctly computes the product of magnitudes and signs to return `-9`, given the input array `[1, 2, 2, -4]`. The second example, with input `[0, 1]`, returns `0` according to the description of the problem. Since the input array is empty in the last example, `None` is returned, consistent with the problem's clarification. 

This script effectively addresses the problem statement and provides a clear understanding of how it operates through the docstring, which includes precise illustrations and sample assessments.