```python
def max_element(l: list) -> int:
    """Returns the maximum element in the list."""
    return max(l)
``` 

This code defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list using the `max` function. 

Here is an example of how to use this function:
```python
print(max_element([1, 2, 3]))  # Outputs: 3
``` 

And here is the expected outcome for the test cases provided:
```bash
123
``` 
```python
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Outputs: 123
``` 

This approach is simple and efficient, directly returning the maximum element without any additional complexities.