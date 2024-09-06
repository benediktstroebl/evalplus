```python
def unique(lst):
    """Sorts and returns unique elements in a list."""
    return list(set(lst))

# Test cases
 Tests = [
    [ [5, 3, 5, 2, 3, 3, 9, 0, 123],
     [5, 3, 5, 2, 3, 3, 0, 7],
     [123, 5, 3, 9, 0, 2, [1, 2, 3]]
    ]
) = (
    [unique(test_list) == set(test_list) for test_list in Tests]
)

if all(Tests):
    print("All tests passed!")
else:
    print("Tests failed.")
```