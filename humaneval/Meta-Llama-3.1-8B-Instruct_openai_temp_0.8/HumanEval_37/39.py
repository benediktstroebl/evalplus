```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indices, while its values at the even indices are equal
    to the values of the even indices of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list l'.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate even and odd indices
    even_indices = [i for i in range(len(l)) if i % 2 == 0]
    odd_indices = [i for i in range(len(l)) if i % 2!= 0]

    # Get the values at even and odd indices
    even_values = [l[i] for i in even_indices]
    odd_values = [l[i] for i in odd_indices]

    # Sort the even values
    sorted_even_values = sorted(even_values)

    # Replace the even values in the list
    sorted_list = [if_else(val, sorted_even_values, odd_values) for val in l]

    return sorted_list

def if_else(val, sorted_even, odd_values):
    if val in sorted_even:
        return sorted_even[sorted_even.index(val)]
    else:
        return val

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```
This script first separates the values at even and odd indices into two separate lists. It then sorts the even values. It replaces the even values in the original list with the sorted even values. If a value is at an odd index, it remains unchanged. The function `if_else` checks whether a value is in the sorted even values list. If it is, it returns the sorted value; otherwise, it returns the original value.