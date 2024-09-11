```markdown
### max_element.py
#### Find the Maximum Element in a List

This script defines a function `max_element` that takes a list as input and returns the maximum element in the list.

```python
def max_element(lst: list):
    """
    Return maximum element in the list.

    Args:
        lst (list): A list of elements.

    Returns:
        The maximum element in the list.

    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    if not lst:
        raise ValueError("List is empty")
    return max(lst)
```

### Example Use Cases

```python
# Test the function with a sample list
numbers = [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]
print(max_element(numbers))  # Output: 123

# Test the function with an empty list
try:
    print(max_element([]))
except ValueError as e:
    print(e)  # Output: List is empty
```

### Running the Script

Save this script to a file named `max_element.py`. Run the script using Python:

```bash
python max_element.py
```

This will execute the script and print the maximum element in the sample list. If you run the script with an empty list, it will raise a `ValueError` as expected.