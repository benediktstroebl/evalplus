```python
def prod_signs(arr):
    result = None
    if arr:
        magnitudes = [abs(x) for x in arr]
        signs = [x > 0 and 1 or x < 0 and -1 or 0 for x in arr]
        result = sum(magnitudes) * prod(signs)
    return result
```
This function calculates the magnitudes of integers in the array and the product of all signs of each number in the array, and then returns their product. It returns `None` for an empty array.

Here's an example usage:
```python
prod_signs([1, 2, 2, -4]) # == -9
prod_signs([0, 1]) == 0
prod_signs([]) == None
``` 
And here is a simpler version of the code using Python's `reduce` function to calculate the product of signs:
```python
def prod_signs(arr):
    return sum([abs(x) for x in arr]) * reduce(lambda x, y: x * y, arr, 1)
``` 
This version is slightly faster.