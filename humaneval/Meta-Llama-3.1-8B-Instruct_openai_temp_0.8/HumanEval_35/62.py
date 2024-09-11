```python
def max_element(lst: list) -> int:
    """
    Return maximum element in the list.
    
    Args:
        lst (list): A list of integers.
    
    Returns:
        int: The maximum element in the list.
    
    Examples:
        >>> max_element([1, 2, 3])
        3
        >>> max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])
        123
    """
    # Check if the list is empty
    if not lst:
        raise ValueError("List is empty")
    
    # Return the maximum element using built-in max function
    return max(lst)


# Test the function
if __name__ == "__main__":
    print(max_element([1, 2, 3]))
    print(max_element([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10]))
```

This script defines a function `max_element` that takes a list of integers as input and returns the maximum element in the list. It uses the built-in `max` function to find the maximum element, which makes the code concise and efficient. The function also includes documentation strings to provide information about its purpose, arguments, and return value. The script also includes test cases to demonstrate the function's usage.