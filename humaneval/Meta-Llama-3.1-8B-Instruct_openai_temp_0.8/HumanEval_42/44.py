```python
def incr_list(l: list):
    """
    Return list with elements incremented by 1.

    Args:
        l (list): The input list.

    Returns:
        list: The list with all elements incremented by 1.
    """
    return [x + 1 for x in l]

# Test cases
if __name__ == "__main__":
    print(incr_list([1, 2, 3]))  # [2, 3, 4]
    print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # [6, 4, 6, 3, 4, 4, 10, 1, 124]
```
This script defines a function `incr_list` that takes a list `l` as input and returns a new list where each element is incremented by 1. The function uses a list comprehension to create the new list. The test cases demonstrate the function's behavior.