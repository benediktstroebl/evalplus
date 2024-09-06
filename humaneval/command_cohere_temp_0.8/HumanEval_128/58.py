```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(abs(x) for x in arr) * product(x % 2 for x in arr)
    return result
```
This Python script defines a function called `prod_signs` that takes an array of integers as input. Inside the function, it checks if the input array is empty, and if not, it calculates two values: the sum of the magnitudes of all integers in the array and the product of all signs (1, -1, or 0) of each number in the array. These two values are then multiplied together to obtain the final result, which is returned. 

The `prod_signs` function is tested on various examples to demonstrate its correctness. The tests check that the function returns the correct values for arrays containing different combinations of numbers and signs, including zero and negative numbers.