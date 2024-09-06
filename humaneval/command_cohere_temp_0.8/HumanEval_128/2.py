```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function uses a list comprehension with a generator expression to calculate the product of the magnitudes and signs of the integers in the array. The result is then returned as the result of the function.

Here is a breakdown of the logic:
1. The function initially checks if the array is empty using the `if arr:` condition. 

2. If the array is not empty, it calculates the sum of magnitudes of integers multiplied by product of all signs using the generator expression `x * y for x, y in zip(arr, arr[1:])`. 

3. The function returns `result`, which is none when the array is empty and the calculated value otherwise. 

This solution is efficient since it uses only one pass through the input array and does not require any additional variables, achieving a time complexity of O(n), where n is the length of the input array.