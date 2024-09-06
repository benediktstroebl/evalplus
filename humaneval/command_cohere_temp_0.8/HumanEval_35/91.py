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

This approach follows the **DRY** (Don't Repeat Yourself) principle, where the functionality to find the maximum element is reused from the built-in `max` function, eliminating the need to reinvent the wheel.