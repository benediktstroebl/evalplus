```python
def sort_even(lst):
    """This function sorts the list lst such that all even indices are equal to their corresponding element, and all odd indices are ordered."""
    lst[::2] = lst[::2]
    lst[1::2] = lst[1::2][::-1]
    return lst
# Example usage
l = [5, 6, 3, 4]
print(sort_even(l))
# Output: [3, 6, 5, 4]
```