```python
def sort_third(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, 
    while its values at the indicies that are divisible by three are equal 
    to the values of the corresponding indicies of l, but sorted.

    Args:
        l (list): The input list.

    Returns:
        list: The list with values at indices divisible by 3 sorted.
    """
    # Separate the list into two parts: values at indices divisible by 3 and others
    div_by_three = [l[i] for i in range(len(l)) if i % 3 == 0]
    others = [l[i] for i in range(len(l)) if i % 3!= 0]

    # Sort the values at indices divisible by 3
    div_by_three.sort()

    # Combine the two parts back into a list
    result = []
    div_index = 0
    for i in range(len(l)):
        if i % 3 == 0:
            result.append(div_by_three[div_index])
            div_index += 1
        else:
            result.append(others.pop(0))

    return result

# Test the function
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```

This script defines the `sort_third` function as specified, and includes two test cases to verify its correctness. It achieves the desired behavior by separating the input list into two parts (values at indices divisible by 3 and others), sorting the first part, and then combining the two parts back into a list.