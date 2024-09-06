```python
def sort_third(lst):
    """Sorts a list l such that numbers less than 3 are at the beginning, and the numbers divisible by 3 are sorted to be at the end.
    """return sorted(lst)[1::3] + sorted(lst)[0:1]

# Test cases
print(sort_third([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Expected output: [2, 6, 3, 4, 8, 9, 5]
```