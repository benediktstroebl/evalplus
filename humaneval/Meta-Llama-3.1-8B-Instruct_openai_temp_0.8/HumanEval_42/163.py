```python
def incr_list(l: list) -> list:
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The input list of integers.

    Returns:
        list: The input list with elements incremented by 1.
    """
    return [x + 1 for x in l]


# Test cases
if __name__ == "__main__":
    import doctest
    doctest.testmod()
```

In this script, we define a function `incr_list` that takes a list of integers as input and returns a new list with each element incremented by 1. We use a list comprehension to achieve this in a concise and efficient manner.

The `doctest` module is used to verify that the function behaves as expected by running the provided test cases. If the function passes all the test cases, the script will exit successfully.