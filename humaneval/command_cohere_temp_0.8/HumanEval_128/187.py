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

Here is a summary of how the code works:
1. The function starts by checking if the input array `arr` is empty. If it's empty, it sets the `result` variable to `None` and returns it immediately since an empty array has no meaningful product of signs.
2. If the array is not empty, it uses two list comprehensions to calculate: 
- `magnitudes`, which is a list of absolute values of each integer in the input array, and 
- `signs`, which is a list of corresponding signs of each integer in the input array. 

3. Then it calculates the result in the following steps:
    - It calculates the sum of the `magnitudes` list with the `sum` function.
    - It calculates the product of the `signs` list with the `prod` function. This function takes a list as argument and returns the product of its elements. 
    - It multiplies the sum of magnitudes by the product of signs to get the desired result.

4. Finally, it returns the result if the input array was not empty, and `None` if the input array was empty. 

This function efficiently solves the problem statement in a straightforward manner.