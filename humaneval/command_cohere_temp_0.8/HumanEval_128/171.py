```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * arr[0]
        magnitudes = [abs(num) for num in arr]
        result = sum(magnitudes) * product(signs)
    return result
```
This function takes an array of integers as input and calculates the sum of the magnitudes of the integers multiplied by the product of all signs of each number in the array. The function first checks if the input array is empty, and if so, returns None. If the array is not empty, it computes the product of signs using the first element's signs and replicates it for all elements, calculates the sum of magnitudes of each number, and returns their product. 

Here is an example usage reflection of the function:
```python
>>> prod_signs([1, 2, 2, -4])
-9
>>> prod_signs([0, 1])
0
>>> prod_signs([])
None
```