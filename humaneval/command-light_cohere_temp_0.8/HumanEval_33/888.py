```python
def sort_third(l: list):
    """Sorts a list l such that values at indices divisible by three are sorted to the front, and the other values are sorted to the back."""
    l = list(sorted(l,key=lambda x: int(x)%3, reverse=True))
    return l

#Test cases
print(sort_third([1, 2, 3]))  # Expected output: [1, 2, 3]
print(sort_third([5, 6, 3, 4, 8, 9, 2]))  # Expected output: [2, 6, 3, 4, 8, 9, 5]
```