```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

# Test the function with a list of various data types and lengths
# Test list of strings (must return strings)
test_func = get_positive(["a", 2, "-3", "five"])
assert test_func == ["a", 2, "five"]

# Test list of numbers (must return numbers)
test_func = get_positive([1, 2, 3, 4, 5])
assert test_func == [1, 2, 3, 4]

# Test list of mixed data (must return integers)
test_func = get_positive([3, "two", 4, 5])
assert test_func == [3, 2, 4]

# Test list of huge numbers (must return numbers)
test_func = get_positive([18777 Llama, 42])
assert test_func == [18777, 42]
```