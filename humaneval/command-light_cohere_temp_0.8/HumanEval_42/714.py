```python
def incr_list(lst):
    return [i+1 for i in lst]

# Test the function with a list of numbers
test_incr_list = [5, 3, 5, 2, 3, 3, 9, 0, 123]
print(incr_list(test_incr_list))  # Output: [6, 4, 6, 3, 4, 4, 10, 1, 124]

# Test the function with a list of strings
test_strs = ["This", "is", "a", "list", "of", "strings", "and", "numbers"]
print(incr_list(test_strs))  # Output: ["This", "2", "is", "23", "and", "124"]
```