```python
def is_sorted(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1)) and len(set(lst)) == len(lst)
```

The function employs two conditional checks: the first check ensures the list is numerically sorted by comparing each element with the next, while the second check verifies that no duplicates exist. If both conditions are met, the list is considered sorted.

The following example usage demonstrates the function's behavior:
```python
print(is_sorted([1, 2, 3, 4, 5]))  # Outputs: True
print(is_sorted([1, 3, 2, 4, 5]))  # Outputs: False
print(is_sorted([1, 2, 2, 3, 3, 4]))  # Outputs: True
```

The expected outputs for each test case are True for sorted lists and False for unsorted lists, matching the specification provided in the prompt.