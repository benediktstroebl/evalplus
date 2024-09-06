```python
def sort_even(lst):
    return lst[:]

# Test the function with an input list
test_list = [1, 2, 3, 4, 5, 6]
result = sort_even(test_list)

# Check the result against the expected output
assert result == [3, 6, 5, 4, 2, 1]
```