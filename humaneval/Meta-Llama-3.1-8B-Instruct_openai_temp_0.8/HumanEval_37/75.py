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
    # Separate the odd and even indices
    odd_indicies = [i for i in range(len(l)) if i % 2!= 0]
    even_indicies = [i for i in range(len(l)) if i % 2 == 0]

    # Sort the elements at even indices
    sorted_even_elements = sorted([l[i] for i in even_indicies])

    # Create the output list with elements at even indices sorted
    output = [0] * len(l)
    for i in odd_indicies:
        output[i] = l[i]
    for i in range(len(even_indicies)):
        output[even_indicies[i]] = sorted_even_elements[i]

    return output

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines the `sort_even` function that sorts elements at even indices of the input list while keeping elements at odd indices unchanged. The test cases demonstrate the function's behavior with two examples.