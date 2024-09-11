```python
def sort_third(l: list):
    """
    This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, 
    while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.

    Args:
        l (list): Input list

    Returns:
        list: Sorted list at indices divisible by three
    """
    return [x if i % 3!= 0 else sorted([y for j, y in enumerate(l) if j % 3 == 0])[k] 
            for k, i, x in enumerate(l)]

# Test cases
print(sort_third([1, 2, 3]))
print(sort_third([5, 6, 3, 4, 8, 9, 2]))
```
This script defines the function `sort_third` as described in the problem statement. It iterates over each element in the input list `l`, and for each element, it checks if its index is divisible by three using the modulo operator (`i % 3!= 0`). If the index is not divisible by three, it leaves the element as is. If the index is divisible by three, it sorts the corresponding elements in the list that are also divisible by three and assigns the result to this position in the output list. The script includes two test cases to demonstrate the function's behavior.