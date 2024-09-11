```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that 
    l' is identical to l in the odd indicies, while its values at the even indicies are equal 
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list with even indicies sorted.
    """
    # Separate even and odd elements from the list
    even_elements = [x for i, x in enumerate(l) if i % 2 == 0]
    odd_elements = [x for i, x in enumerate(l) if i % 2!= 0]

    # Sort the even elements
    sorted_even_elements = sorted(even_elements)

    # Combine the sorted even elements with the odd elements
    return [x if i % 2!= 0 else y for i, x in enumerate(l) for y in sorted_even_elements]

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines the function `sort_even` as specified, and includes two test cases to verify its correctness. The function uses list comprehensions to separate even and odd elements from the input list, sorts the even elements, and then combines the sorted even elements with the odd elements to produce the output.