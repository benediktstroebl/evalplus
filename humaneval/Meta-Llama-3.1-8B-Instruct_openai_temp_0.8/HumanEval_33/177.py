```python
def sort_third(lst: list) -> list:
    """
    This function takes a list lst and returns a list lst' such that
    lst' is identical to lst in the indices that are not divisible by three, 
    while its values at the indices that are divisible by three are equal 
    to the values of the corresponding indices of lst, but sorted.

    Args:
        lst (list): The input list.

    Returns:
        list: The modified list.
    """
    # Separate the list into two parts, one where the indices are divisible by 3
    # and the other where they are not.
    div_by_three = [lst[i] for i in range(len(lst)) if i % 3 == 0]
    not_div_by_three = [lst[i] for i in range(len(lst)) if i % 3!= 0]

    # Sort the list where the indices are divisible by 3.
    sorted_div_by_three = sorted(div_by_three)

    # Combine the two parts back into one list, with the sorted part where the 
    # indices are divisible by 3.
    result = [None] * len(lst)
    for i in range(len(lst)):
        if i % 3 == 0:
            result[i] = sorted_div_by_three.pop(0)
        else:
            result[i] = not_div_by_three.pop(0)

    return result

# Example usage:
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```

This Python function `sort_third` takes a list of numbers as input, separates it into two lists (one where the index is divisible by 3 and the other where it is not), sorts the first list, and then combines the two lists back together in the original order, replacing the original numbers at indices divisible by 3 with the sorted numbers.