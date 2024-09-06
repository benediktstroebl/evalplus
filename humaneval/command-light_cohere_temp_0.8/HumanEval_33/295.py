```python
def sort_third(l: list):
    """Sorts list l such that values divisible by three appear at the beginning and values not divisible by three appear in the rest of the list, but in original order."""
    l = [3, 6, 1, 2, 4, 5, 8, 9]
    return [i if i % 3 == 0 else i for i in l]

# Test cases
print(sort_third([1, 2, 3]))    # Expected: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2])) # Expected: [2, 6, 3, 4, 8, 9, 5]
```