```python
def sort_even(l: list):
    return sorted(l, key=lambda x: (x if x % 2 == 0 else x + 1))

# Test the function with a list of numbers
# Ensure the function returns the expected results
[test_list] = [1, 2, 3]
[test_list] = [5, 6, 3, 4]
[test_list] = [8, 9, 10, 11]

# Sort the list using the function
sorted_list = sort_even([test_list])

# Check the results against the expected results
assert sorted_list == [3, 6, 5, 4]
assert sorted_list == [1, 2, 3, 5, 6, 4, 8, 9, 10, 11]

# Output:
```