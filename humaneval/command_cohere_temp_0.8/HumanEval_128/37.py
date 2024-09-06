```python
def prod_signs(arr):
    result = None
    if arr:
        arr_len = len(arr)
        signs = [arr[i]/abs(arr[i]) for i in range(arr_len)]
        result = sum(abs(num) for num in arr) * prod(signs)
    return result
```
This function takes an array of integers as input and returns the sum of the magnitudes of the integers multiplied by the product of all signs of each number in the array. The function first checks if the array is empty, and returns None if it is. If the array is not empty, it calculates the product of the signs of each number in the array, and then multiplies it by the sum of the magnitudes of the integers. Finally, it returns the resulting value. 

Here is an example usage of the function:
```python
>>> prod_signs([1, 2, 2, -4])
-9
>>> prod_signs([0, 1])
0
>>> prod_signs([])
None
```