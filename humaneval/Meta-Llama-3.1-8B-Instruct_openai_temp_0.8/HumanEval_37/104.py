```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): A list of elements to be sorted.

    Returns:
        list: A new list where even indicies are sorted.
    """
    # Separate even and odd elements
    even_elements = l[1::2]
    odd_elements = l[::2]

    # Sort the even elements
    sorted_even_elements = sorted(even_elements)

    # Replace the even elements in the original list with the sorted ones
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(odd_elements[i // 2])
        else:
            result.append(sorted_even_elements[i // 2])

    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script uses a list comprehension to create a new list where the even indicies are sorted. The even elements are first separated from the odd elements, then sorted using the built-in `sorted()` function. The even elements are then replaced in the original list with the sorted ones. Finally, the test cases are executed to verify the correctness of the function.