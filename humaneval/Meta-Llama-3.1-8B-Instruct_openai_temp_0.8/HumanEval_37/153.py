```python
def sort_even(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.
        
    Returns:
        list: The modified list with even indices sorted.
    """
    # Separate the list into odd and even indices
    odd_indices = l[1::2]
    even_indices = sorted(l[::2])
    
    # Combine the sorted even indices with the odd indices
    result = []
    for i, val in enumerate(l):
        if i % 2 == 0:
            result.append(even_indices[i // 2])
        else:
            result.append(odd_indices[i // 2])
    
    return result

# Test cases
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script defines the `sort_even` function as specified and includes two test cases to demonstrate its functionality. The function works by first separating the input list into two lists: one containing the values at odd indices and another containing the values at even indices. It then sorts the list of even indices. The function combines the sorted even indices with the odd indices to produce the desired output.