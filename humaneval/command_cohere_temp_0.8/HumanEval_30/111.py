```python
def get_positive(l: list):
    return [x for x in l if x > 0]
```

The function `get_positive` uses a list comprehension to filter the elements of the input list `l` and returns only those elements that are greater than zero. 

The behaviour of the function is demonstrated in the docstring using python's assert statements to test the function with example inputs. 

To further illustrate the functionality here's an example of how to use the `get_positive` function: 
 ```python
>>> get_positive([-1, 2, -4, 5, 6])
[2, 5, 6]
>>> get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
[5, 3, 2, 3, 9, 123, 1]
``` 

As shown, the expected behaviour of the function is to return the list with all the positive numbers. 

If there are any further questions or suggestions on how to improve the function feel free to let me know!