```python
def sort_third(lst):
    """Sorts the list lts such that values at indices divisible by three are moved to the front, while other values are left as they are.
    return a dry-sorted list.
    """
   
        constant-time list of lists."""
    lst = [x for x in lst if x % 3 != 0] + [x for x in lst if x % 3 == 0]
    return lst

# Test cases for the function
test_sort_third = [
    [
        [1, 2, 3],
        [5, 6, 3, 4, 8, 9, 2],
        [0, 1, 2, 3]
    ]
]

# Function call and print results
print(sort_third(test_sort_third))
```