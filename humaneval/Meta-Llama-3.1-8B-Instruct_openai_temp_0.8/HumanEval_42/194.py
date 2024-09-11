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
print(incr_list([1, 2, 3]))  # Expected output: [2, 3, 4]
print(incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123]))  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```

This script defines a function `incr_list` that takes a list `l` as input, uses a list comprehension to create a new list where each element is incremented by 1, and returns the result. It then tests the function using the provided test cases. 

Alternatively, if you want to modify the original list in-place (which is generally not recommended for functional operations), you can use the following version of the function:

```python
def incr_list_in_place(l: list):
    """
    Modify the input list in-place by incrementing each element by 1.

    Args:
        l (list): The input list.
    """
    for i in range(len(l)):
        l[i] += 1

# Test cases
l = [1, 2, 3]
incr_list_in_place(l)
print(l)  # Expected output: [2, 3, 4]

l = [5, 3, 5, 2, 3, 3, 9, 0, 123]
incr_list_in_place(l)
print(l)  # Expected output: [6, 4, 6, 3, 4, 4, 10, 1, 124]
```