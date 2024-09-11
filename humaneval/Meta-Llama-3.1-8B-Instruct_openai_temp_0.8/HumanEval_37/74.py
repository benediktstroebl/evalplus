### Python Script to Sort Even Indices

```python
def sort_even(l: list) -> list:
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The list with even indices sorted.
    """
    # Separate the elements at odd and even indices into two lists
    odd_elements = [element for index, element in enumerate(l) if index % 2!= 0]
    even_elements = [element for index, element in enumerate(l) if index % 2 == 0]

    # Sort the elements at even indices
    even_elements.sort()

    # Combine the sorted even elements with the odd elements
    result = []
    for index in range(len(l)):
        if index % 2 == 0:
            result.append(even_elements[index // 2])
        else:
            result.append(odd_elements[(index - 1) // 2])

    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script uses a list comprehension to separate the elements at odd and even indices into two lists, sorts the even elements, and then combines them back into the original list structure. The test cases demonstrate the function's correctness.