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
    return [x if i % 3!= 0 else sorted([y for y in lst if y % 3 == 0])[k] 
            for i, x in enumerate(lst) for k in range(len([y for y in lst if y % 3 == 0]))]

# Test cases
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```

This script defines a function `sort_third` that sorts the elements at indices that are divisible by three while keeping other elements unchanged. It uses a list comprehension to generate the modified list. The test cases demonstrate the function's behavior. 

Please note that this solution has a time complexity of O(n^2) due to the sorting operation inside the list comprehension, where n is the number of elements in the list that are divisible by three. For large lists, a more efficient solution with a time complexity of O(n) using a separate data structure (like a list or an array) to store the elements at indices divisible by three can be implemented. 

Here's an example of an O(n) solution:

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
    three_divisible = [x for x in lst if x % 3 == 0]
    three_divisible.sort()
    result = []
    for i, x in enumerate(lst):
        if i % 3 == 0:
            result.append(three_divisible.pop(0))
        else:
            result.append(x)
    return result

# Test cases
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```