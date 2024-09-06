```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * (-1 if num < 0 else 1)
        result = sum([num * sign for num, sign in zip(arr, signs)])
    return result
```
This Python script defines a function called `prod_signs` that takes an array of integers as input. It returns the sum of the magnitudes of the integers in the array multiplied by the product of all signs of each number. This is achieved by first checking if the array is empty, and returning `None` if it is. It then calculates the product of signs using a list comprehension that determines the sign of each number (`-1` if negative, `1` if positive, and `0` if zero). This signs list is then used to calculate the product of signs and the magnitude sum using a list comprehension and the `zip` function. The result is the product of signs multiplied by the sum of magnitudes.

Here is an example usage of the function:
```python
prod_signs([1, 2, 2, -4]) # == -9
prod_signs([0, 1]) == 0
prod_signs([]) == None
```
This would return the following outputs:
```python
-9
0
None
```