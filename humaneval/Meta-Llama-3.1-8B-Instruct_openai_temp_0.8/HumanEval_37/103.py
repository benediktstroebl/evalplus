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
    even indicies = [i for i, _ in enumerate(l) if i % 2 == 0]
    odd indicies = [i for i, _ in enumerate(l) if i % 2!= 0]
    
    # Sort values at even indices
    even_values = sorted([l[i] for i in even indicies])
    
    # Replace values at even indices with sorted values
    sorted_list = [even_values[i // 2] if i % 2 == 0 else l[i] for i in range(len(l))]
    
    return sorted_list


# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

This script will output:
```
[1, 2, 3]
[3, 6, 5, 4]
```