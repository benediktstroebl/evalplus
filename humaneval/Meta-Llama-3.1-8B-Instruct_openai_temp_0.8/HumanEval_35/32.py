### Maximum Element in a List
#### Problem Description
Return the maximum element in a list.

#### Solution
```python
def max_element(l: list):
    """
    Return maximum element in the list.

    Args:
        l (list): A list of elements.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not l:  # Check if the list is empty
        raise ValueError("List is empty")
    return max(l)  # Return the maximum element in the list
```
#### Explanation
This script defines a function `max_element` that takes a list `l` as input and returns its maximum element. The function uses the built-in `max` function in Python to find the maximum element in the list. If the list is empty, the function raises a `ValueError` to indicate that the list cannot be processed.

#### Usage
To use this script, save it to a file (e.g., `max_element.py`) and run it from the command line:
```bash
python max_element.py
```
You can test the function using the examples provided in the docstring:
```python
print(max_element([1, 2, 3]))  # Output: 3
print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))  # Output: 123
```