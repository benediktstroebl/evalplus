```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Unit tests
test_get_positive = unittest.TestCase("get_positive")
test_get_positive.setUp [list([-1, 2, -4, 5, 6])
test_get_positive.setUplist([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])

# Call test suite and display results
test_get_positive.test()
failures=False
test_results = test_get_positive.results
print('Test Results:')
for test in test_results:
    print(test)

```