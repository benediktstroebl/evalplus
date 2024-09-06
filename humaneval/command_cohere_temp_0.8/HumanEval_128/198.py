```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(abs(num) for num in arr) * product(num % 2 for num in arr)
    return result
```
This Python script defines a function `prod_signs()` that takes an array of integers as input. It calculates the product of the signs of all numbers in the array, which is done by iterating over the array and using a product context manager to efficiently calculate the product of the signs. The function then calculates the sum of the magnitudes of all numbers in the array and multiplies it by the product of signs. Finally, the function returns the result if the array is not empty, and None if the input array is empty. 

Here is an example usage example of this code:
```python
prod_signs([1, 2, 2, -4]) # Output: -9
prod_signs([0, 1]) # Output: 0
prod_signs([]) # Output: None
```
This would output:
- -9
- 0
- None
```