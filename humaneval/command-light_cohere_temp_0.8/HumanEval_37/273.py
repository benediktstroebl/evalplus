```python
def sort_even(lst):
    """Sorts the list l such that the values at even indices are equal to each other"""
    return sorted(lst,key=lambda x: x % 2)

# Test the function with a list of numbers
test_list = [5, 6, 3, 4]
# Call the function and pass the test_list
result = sort_even(test_list)

# Check the result against the expected output
# [(3, 6, 5, 4)]
assert result == [3, 6, 5, 4]
```