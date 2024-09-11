### Even Index Sorting Function

Here's a Python function that fulfills the provided requirements:

```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Parameters:
    l (list): The input list to be sorted on even indices.

    Returns:
    list: A new list with even indices sorted.

    >>> sort_even([1, 2, 3])
    [1, 2, 3]
    >>> sort_even([5, 6, 3, 4])
    [3, 6, 5, 4]
    """
    # Separate the even and odd elements from the input list
    even_elements = l[::2]
    odd_elements = l[1::2]

    # Sort the even elements in ascending order
    even_elements.sort()

    # Interleave the sorted even elements with the odd elements to get the result
    result = [x for pair in zip(even_elements, odd_elements) for x in pair] + even_elements[len(odd_elements):]

    return result
```

### Example Usage

Here's how you can use the `sort_even` function:

```python
# Test the function with the provided examples
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```