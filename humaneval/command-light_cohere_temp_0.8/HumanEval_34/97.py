```python
def unique(lst):
    seen = set()
    return [x for x in lst if x not in seen and x not in [0]]

# Test case 1: Unique elements from a list
test_case1 = [5, 3, 5, 2, 3, 3, 9, 0, 123]
result1 = unique(test_case1)
assert result1 == [0, 2, 3, 5, 9, 123]

# Test case 2: Unique elements from a generator
test_case2 = list(range(1, 10))
result2 = unique(test_case2)
assert len(result2) == 10
assert result2 == list(set(test_case2))

# If this worked well, you could copy-paste this code into an interactive Python environment or your preferred code editor, and run it to verify the results.