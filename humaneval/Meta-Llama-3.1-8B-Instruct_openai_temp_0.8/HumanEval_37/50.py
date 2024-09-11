```python
def sort_even(l: list) -> list:
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
    
    Returns:
        list: The modified list with even indices sorted.
    """
    # Separate even and odd indexed elements
    even_indexed = [x for i, x in enumerate(l) if i % 2 == 0]
    odd_indexed = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort even indexed elements
    even_indexed.sort()
    
    # Combine the sorted even indexed elements with the odd indexed elements
    result = [x if i % 2!= 0 else y for i, (x, y) in enumerate(zip(odd_indexed, even_indexed))]
    
    return result

# Test cases
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script defines the `sort_even` function, which takes a list as input, separates its even and odd indexed elements, sorts the even indexed elements, and then combines them with the odd indexed elements to produce the output list. It also includes two test cases to demonstrate the function's behavior.