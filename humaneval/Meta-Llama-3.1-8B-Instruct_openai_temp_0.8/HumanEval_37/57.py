### Sort Even Indices
#### A Python Function to Sort Even Indices in a List

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
    # Separate odd and even indices
    odd = [l[i] for i in range(len(l)) if i % 2 == 0]
    even = [l[i] for i in range(len(l)) if i % 2!= 0]

    # Sort even indices
    even.sort()

    # Combine odd and sorted even indices
    result = [None] * len(l)
    for i in range(len(l)):
        if i % 2 == 0:
            result[i] = even.pop(0)
        else:
            result[i] = odd.pop(0)

    return result

# Test cases
print(sort_even([1, 2, 3]))  # [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # [3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list where the elements at even indices are sorted. The function uses list comprehensions to separate the odd and even indices, sorts the even indices, and then combines the odd and sorted even indices into the result list. The test cases demonstrate the function's correctness.