```python
def sort_even(lst: list) -> list:
    """
    This function takes a list lst and returns a list lst' such that
    lst' is identical to lst in the odd indices, while its values at the even indices are equal
    to the values of the even indices of lst, but sorted.

    Args:
        lst (list): The input list.

    Returns:
        list: The modified list.
    """
    even_indices = [lst[i] for i in range(len(lst)) if i % 2 == 0]
    sorted_even_indices = sorted(even_indices)
    
    result = []
    even_index = 0
    for i in range(len(lst)):
        if i % 2 == 0:
            result.append(sorted_even_indices[even_index])
            even_index += 1
        else:
            result.append(lst[i])
    
    return result


# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines a function `sort_even` that takes a list as input, sorts the elements at even indices, and returns the modified list. The test cases demonstrate the function's behavior with sample inputs.