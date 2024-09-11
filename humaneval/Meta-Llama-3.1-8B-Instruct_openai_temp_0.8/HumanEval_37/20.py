Here's a self-contained Python script that solves the given problem:

```markdown
### Even Index Sorting Function

This script defines a Python function `sort_even` which sorts the values at even indices in a list, 
while keeping the values at odd indices unchanged.

```python
def sort_even(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the odd indicies, while its values at the even indicies are equal
    to the values of the even indicies of l, but sorted.
    
    Args:
        l (list): The input list.

    Returns:
        list: The list with even indices sorted.

    Examples:
        >>> sort_even([1, 2, 3])
        [1, 2, 3]
        >>> sort_even([5, 6, 3, 4])
        [3, 6, 5, 4]
    """
    # Separate the values at even and odd indices
    even_values = sorted([l[i] for i in range(len(l)) if i % 2 == 0])
    odd_values = [l[i] for i in range(len(l)) if i % 2!= 0]
    
    # Combine the sorted even values with the unchanged odd values
    return [even_values[i // 2] if i % 2 == 0 else odd_values[i // 2] for i in range(len(l))]

# Example usage:
print(sort_even([1, 2, 3]))  # Output: [1, 2, 3]
print(sort_even([5, 6, 3, 4]))  # Output: [3, 6, 5, 4]
```

This script first separates the values at even and odd indices using list comprehensions. 
Then it sorts the even values and combines them with the unchanged odd values. 
Finally, it prints the results for the given example inputs.