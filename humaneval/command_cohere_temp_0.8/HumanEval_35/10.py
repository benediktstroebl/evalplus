```python
def max_element(l: list) -> int:
    """Returns the maximum element in the list."""
    return max(l)
``` 

This code defines a function called `max_element` that takes a list `l` as input and returns the maximum element in the list using the `max` function. 

Here is an example of how to use this function:
```python
print(max_element([1, 2, 3]))  # 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # 123
``` 

The function returns the maximum element in the list, which in this case is `3` in the first example and `123` in the second. 

This approach directly leverages the `max` function as a more efficient and simpler way to achieve the desired result, making the code more concise and readable.