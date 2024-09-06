```python
def sort_even(lst):
    """Sorts an input list l such that values at even indices are sorted to
    appear in ascending order, while the rest of the values remain unchanged."""
    lst[:] = sorted(lst[:], key=lambda x: x if x % 2 == 0 else x - 1)
    return lst

# Example usage
my_list = [5, 6, 3, 4]
result = sort_even(my_list)
print(result)  # Expected output: [3, 6, 5, 4]
```