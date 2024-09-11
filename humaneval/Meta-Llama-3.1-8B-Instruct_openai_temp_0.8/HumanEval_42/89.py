```python
def incr_list(l: list):
    """
    Return a new list with elements incremented by 1.

    Args:
        l (list): Input list of integers.

    Returns:
        list: List with elements incremented by 1.
    """
    return [x + 1 for x in l]


# Test cases
if __name__ == "__main__":
    print(incr_list([1, 2, 3]))  # [2, 3, 4]
    print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script uses a list comprehension to create a new list where each element is incremented by 1. The test cases are included to demonstrate the function's behavior. The `if __name__ == "__main__":` block is used to ensure the tests run only when the script is executed directly, not when it's imported as a module.