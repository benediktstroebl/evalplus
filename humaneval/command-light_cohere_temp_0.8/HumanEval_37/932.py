```python
def sort_even(lst):
    """This function sorts a list l such that the even indices are in the same order as their original values, while maintaining the relative order of the odd indices."""
    return lst[: len(lst) // 2] + lst[-len(lst) - len(lst) // 2:]

# Test the function with a simple list
test_list = [1, 2, 3]
result = sort_even(test_list)
print(result)  # Expected output: [1, 2, 3]

# Test the function with a list of different lengths
test_list_with_mixed_lengths = [5, 6, 3, 4]
result = sort_even(test_list_with_mixed_lengths)
print(result)  # Expected output: [3, 6, 5, 4]

# Test the function with a list of even lengths ( duplicates allowed )
test_list_even_length = [2, 2, 4, 2, 2]
result = sort_even(test_list_even_length)
print(result)  # Expected output: [2, 2, 2, 4, 2]
```