```markdown
### Maximum Element in a List

This Python script defines a function `max_element` that takes a list as input and returns the maximum element in the list.

#### Code

```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): A list of elements.

    Returns:
        Any: The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    return max(l)

# Example usage:
numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(numbers))
```

#### How it Works

The `max_element` function uses the built-in `max` function in Python, which returns the largest item in an iterable or the largest of two or more arguments.

In this script, we define the `max_element` function with a docstring that explains its purpose, parameters, and return value. We then provide an example usage of the function with a list of numbers.

You can run this script in your Python environment to test the `max_element` function.