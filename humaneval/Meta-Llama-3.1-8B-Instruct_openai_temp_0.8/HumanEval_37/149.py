```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The sorted list according to the problem statement.
    """
    # Separate the even and odd indexed elements into two different lists
    even_indexed = [x for i, x in enumerate(l) if i % 2 == 0]
    odd_indexed = [x for i, x in enumerate(l) if i % 2!= 0]
    
    # Sort the even indexed elements
    even_indexed.sort()
    
    # Combine the sorted even indexed elements with the odd indexed elements
    return [x if i % 2!= 0 else even_indexed[i // 2] for i, x in enumerate(l)]

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script will output:
```
[1, 2, 3]
[3, 6, 5, 4]
```
The function `sort_even` takes a list `l` as input, separates the even and odd indexed elements into two different lists, sorts the even indexed elements, and then combines the sorted even indexed elements with the odd indexed elements. The result is a new list that is identical to the input list in the odd indices, but has the even indexed elements sorted.