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
    # Separate odd and even indexed elements
    odd = [l[i] for i in range(len(l)) if i % 2!= 0]
    even = [l[i] for i in range(len(l)) if i % 2 == 0]
    
    # Sort the even indexed elements
    even.sort()
    
    # Combine the two lists, replacing the even indexed elements with the sorted ones
    result = []
    for i in range(len(l)):
        if i % 2 == 0:
            result.append(even[i // 2])
        else:
            result.append(odd[i // 2])
    
    return result

# Test the function
print(sort_even([1, 2, 3]))
print(sort_even([5, 6, 3, 4]))
```

Output:
```
[1, 2, 3]
[3, 6, 5, 4]
```

This script defines a function `sort_even` that takes a list `l` as input and returns a new list where the even indexed elements are sorted. It first separates the odd and even indexed elements into two separate lists, sorts the even indexed elements, and then combines the two lists by replacing the even indexed elements with the sorted ones. The function is then tested with the provided example inputs.