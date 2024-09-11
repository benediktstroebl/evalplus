```python
def sort_third(l: list):
    """This function takes a list l and returns a list l' such that
    l' is identical to l in the indicies that are not divisible by three, while its values at the indicies that are divisible by three are equal
    to the values of the corresponding indicies of l, but sorted.
    >>> sort_third([1, 2, 3])
    [1, 2, 3]
    >>> sort_third([5, 6, 3, 4, 8, 9, 2])
    [2, 6, 3, 4, 8, 9, 5]
    """
    return [x if i%3!= 0 else sorted([y for j, y in enumerate(l) if j%3 == 0])[k] 
            for k, (i, x) in enumerate(zip(range(len(l)), l))]

# Test the function
print(sort_third([1, 2, 3]))  # [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # [2, 6, 3, 4, 8, 9, 5]
```
This script uses list comprehension to iterate over the input list `l`. For each index `i`, it checks if `i` is divisible by 3. If it is, it selects the corresponding sorted value from `l`. If it's not, it leaves the original value unchanged. The result is a new list that meets the problem's requirements.