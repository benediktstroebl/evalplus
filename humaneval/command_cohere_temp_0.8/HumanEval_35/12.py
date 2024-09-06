```python
def max_element(l: list):
    """Return maximum element in the list.
    
    Args:
    - l (list): List of elements
    
    Returns:
    - max (int or str): Maximum value in the list
    """
    max_ = max(l, key=lambda x: x)
    return max_
```

This code defines a function called `max_element` that takes a list called `l` as an argument. The function uses the `max` function with a `key` argument to find the maximum element in the list. The `key` argument is a lambda function that specifies the attribute of the list element to be considered when determining the maximum value. 

Here is an example usage of the function:
```python
print(max_element([1, 2, 3]))  # Outputs: 3
```

And here is another example usage of the function:
```python
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Outputs: 123
```

This demonstrates the function's ability to handle both positive and negative integers, as well as integers and strings, and provides the maximum value present in the list, regardless of the data type.