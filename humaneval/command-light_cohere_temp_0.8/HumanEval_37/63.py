```python
def sort_even(l: list):
    """Sorts the list l such that all even index values are equal, and the list appears in ascending order."""
    l = list(set(l) & set(range(len(l))))
    return sorted(l)

# Example: [1, 2, 3]
# Should return: [1, 2, 3]
test_data = [5, 6, 3, 4]
test_result = sort_even(test_data)
print("Test Result:", test_result) # Output: [3, 6, 5, 4]
```