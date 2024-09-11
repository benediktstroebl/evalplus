```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list

    Returns:
        list: The sorted list
    """
    # Separate odd and even indices
    odd = [l[i] for i in range(len(l)) if i % 2!= 0]
    even = [l[i] for i in range(len(l)) if i % 2 == 0]

    # Sort the even indices
    even.sort()

    # Combine the results, keeping odd indices unaffected
    result = [None] * len(l)  # Initialize result with None
    for i in range(len(l)):
        if i % 2!= 0:  # If index is odd, copy from the original list
            result[i] = l[i]
        else:  # If index is even, copy from the sorted list
            result[i] = even[i // 2]  # Use integer division to get the correct index

    return result

# Example usage:
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script achieves the desired behavior by first separating the odd and even indices of the input list `l`. It then sorts the values at the even indices and combines them back into the result, keeping the odd indices unaffected. The example usage demonstrates the function's behavior with the provided test cases.