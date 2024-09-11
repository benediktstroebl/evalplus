```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The modified list.
    """
    # Separate even and odd indices
    even_indices = [x for x in range(len(l)) if x % 2 == 0]
    odd_indices = [x for x in range(len(l)) if x % 2!= 0]

    # Get the values at even and odd indices
    even_values = [l[i] for i in even_indices]
    odd_values = [l[i] for i in odd_indices]

    # Sort the even values
    even_values.sort()

    # Combine the even and odd values into the output list
    output = [x for x in odd_values] + even_values
    assert len(output) == len(l)
    return output

# Test the function
print(sort_even([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Expected output: [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list where the values at even indices are sorted, while the values at odd indices remain unchanged. The function uses list comprehensions to separate the even and odd indices, sort the even values, and combine the even and odd values into the output list. The script includes test cases to verify the correctness of the function.