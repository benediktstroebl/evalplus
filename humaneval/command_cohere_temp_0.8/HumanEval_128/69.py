```python
def prod_signs(arr):
    result = None
    if arr:
        result = sum(x * y for x, y in zip(arr, arr[1:]))
    return result
```
This function uses a list comprehension to calculate the product of the signs of each number in the array. If the array is empty, it returns `None`. 

Here is a test case to test the function:
```python
assert prod_signs([1, 2, 2, -4]) == -9
``` 

And here is another test case: 
```python
assert prod_signs([0, 1]) == 0
``` 

Lastly, here is a test case to demonstrate what happens when an empty list is input:
```python
assert prod_signs([]) is None
``` 

This test suite should help verify the functionality of the provided function.