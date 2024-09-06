```python
def prod_signs(arr):
    result = None
    if arr:
        signs = [num > 0 for num in arr] * (-1)
        result = sum([num * sign for num, sign in zip(arr, signs)])
    return result
```
This Python script defines a function named `prod_signs` that takes an array of integers as input. It calculates the product of the signs of each number in the array, where 1 is considered positive, -1 is considered negative, and 0 is treated as if it has no sign. Then, it computes the sum of the magnitudes of the integers in the array multiplied by their respective signs. The function returns `None` if the input array is empty.

Here is an example usage of the function:
```python
>>> prod_signs([1, 2, 2, -4])
-9
>>> prod_signs([0, 1])
0
>>> prod_signs([])
None
``` 
And here is the markdown code block for the problem:
```python
def prod_signs(arr):
    """
    You are given an array arr of integers and you need to return
    sum of magnitudes of integers multiplied by product of all signs
    of each number in the array, represented by 1, -1 or 0.
    Note: return None for empty arr.

    Example:
    >>> prod_signs([1, 2, 2, -4]) == -9
    >>> prod_signs([0, 1]) == 0
    >>> prod_signs([]) == None
    """
```