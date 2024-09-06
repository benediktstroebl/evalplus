```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array and product of all signs of each number in the array and returns their product. The result is `None` for an empty array.

Here's how the function works step by step:
1. `result = None`: Initialize result to None. This is a common convention to indicate that the function hasn't computed any value yet.
2. `if arr`: Check if the input array `arr` is not empty. If it's not empty, proceed to calculate the result; otherwise, return `None` immediately.
3. `magnitudes = [abs(x) for x in arr]`: Calculate the magnitudes of each integer in the array. The `abs()` function returns the absolute value of a number, so it removes the negative sign. By using a list comprehension, we create a list of magnitudes from the array.
4. `signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]`: Calculate the signs of each number in the array. If a number is positive, it gets the sign 1; if it's negative, it gets the sign -1; if it's exactly 0, it gets 0. Again, using a list comprehension captures this sign information.
5. `result = sum(magnitudes) * prod(signs)`: Calculate the final result. First, the `sum()` function calculates the sum of the magnitudes, and `prod()` calculates the product of the signs. Multiplying these two values gives the desired result.
6. Return `result`: Return the computed result or `None` if the input array was empty. 

This function is carefully structured to handle different scenarios and provide the correct result based on the given description.