```python
def get_positive(lst):
    """Return only positive numbers in the list"""
    return [num for num in lst if num >= 0]

# Unit tests
test_get_positive = []
test_items = [([]], [0, 2, -4, 5, 6])
test_get_positive.push_test(get_positive, test_items[0])
test_get_positive.push_test(get_positive, test_items[1])

# Test results
test_results = {
    "get_positive": [test_value] == test_items[0][0] and \
            [test_value] == test_items[1][0] and
            all([num >= 0 for num in test_items[0]]) and
            all([num >= 0 for num in test_items[1]])]
}

print(test_results)
```