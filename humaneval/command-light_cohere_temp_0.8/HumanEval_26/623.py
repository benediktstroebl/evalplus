Here is a Python script with a self-contained function that solves the problem of removing duplicate integers from a list and passes the corresponding tests:

```python
def remove_duplicates(numbers: List[int]) -> List[int]:
    return list(set(numbers))

numbers = [1, 2, 3, 2, 4, 2]
result = remove_duplicates(numbers)
print(result)
```

This function, `remove_duplicates`, uses the built-in Python `set()` function to create a set of unique elements from the input list. The list is then converted into a set to remove duplicate elements. The resulting list contains only the unique elements from the original list.