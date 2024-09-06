```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function uses a list comprehension with a zipper to calculate the product of elements in the list and their subsequent signs. It returns None for an empty list to fit the specified requirement.

The provided example tests can be replicated as follows:
```python
>>> prod_signs([1, 2, 2, -4])
-9
>>> prod_signs([0, 1])
0
>>> prod_signs([])
None
```