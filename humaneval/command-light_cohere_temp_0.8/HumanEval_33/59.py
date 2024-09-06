```python
def sort_third(lst):
    """This function sorts a list l according to the criteria that numbers not divisible by three come first,
    while numbers divisible by three are placed in the same order as in l."""
    lst[::3] = lst[::3].copy()
    return sorted(lst)

# Test cases
print(sort_third([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Expected output: [2, 6, 3, 4, 8, 9, 5]
```