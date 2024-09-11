```python
def unique(lst: list):
    """Return sorted unique elements in a list"""
    return sorted(set(lst))

# Test the function
print(unique([5, 3, 5, 2, 3, 3, 9, 0, 123]))
# Output: [0, 2, 3, 5, 9, 123]
```

Explanation:
- This script defines a function `unique` that takes a list `lst` as input.
- It removes duplicates by converting the list to a set, which automatically removes duplicate elements.
- It sorts the resulting set in ascending order using the `sorted` function.
- The function returns the sorted set of unique elements.
- The test at the end of the script calls the function with the provided example list and prints the result.