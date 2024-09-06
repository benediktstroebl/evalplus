```python
def get_positive(lst):
    return [x for x in lst if x >= 0]

# Test the function with various inputs
assertEqual(get_positive([-1, 2, -4, 5, 6]) , [2, 5, 6])
assertEqual(get_positive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]) , [5, 3, 2, 3, 9, 123, 1])
```
The function `get_positive` takes a list as an argument and returns a new list containing only the positive elements from the original list. 

In the above code, we test the `get_positive` function with two inputs. We use the above `assertEqual` function to verify that the returned values from the `get_positive` function are correct.