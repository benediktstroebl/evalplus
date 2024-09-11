```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): Input list.
    
    Returns:
        list: Sorted list according to the problem description.
    """
    # Separate odd and even indicies into two different lists
    odd = [num for i, num in enumerate(l) if i % 2!= 0]
    even = [num for i, num in enumerate(l) if i % 2 == 0]
    
    # Sort the even list
    even.sort()
    
    # Create a new list where odd indicies are the same and even indicies are sorted
    sorted_l = []
    for i, num in enumerate(l):
        if i % 2 == 0:
            sorted_l.append(even[i // 2])
        else:
            sorted_l.append(num)
    
    return sorted_l

# Test cases
print(sort_even([1, 2, 3]))  # Expected: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Expected: [3, 6, 5, 4]
```

This script defines a function called `sort_even` that solves the specified problem. The function works by separating the input list into two lists, `odd` and `even`, based on their indices. It then sorts the `even` list and creates a new list, `sorted_l`, where the odd indices are the same as the original list and the even indices are the sorted `even` list. The function returns this new list. The script includes two test cases to verify the function's correctness.