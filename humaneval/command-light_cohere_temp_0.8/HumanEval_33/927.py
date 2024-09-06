```python
def sort_third(lst):
    """This function sorts a list such that values divisible by three are in their correct positions."""
    return sorted(lst, key=lambda x: x // 3)

# Test the function
list_test = [1, 2, 3, 6, 4, 8, 9]
print(sort_third(list_test))  # expected output: [2, 6, 3, 4, 8, 9, 1, 5]
```