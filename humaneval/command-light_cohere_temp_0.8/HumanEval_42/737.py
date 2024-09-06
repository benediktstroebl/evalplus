```python
def incr_list(l: list):
    """Return list with elements incremented by 1."""
    new_list = [x + 1 for x in l]
    return new_list

# Test cases
test_incr_list = [
    dict(zip(['input'], [1, 2, 3])),
    dict(zip(['expected'], [2, 3, 4])),
    # Invalid: list of strings
    dict(zip(['input'], ['a', 'b'])),
    # Invalid: not list
    dict(zip(['input'], [10, 20, 30])),
]

# Execute tests
results = incr_list(**test_incr_list)

# Print results
print("Test Results:")
for result, (test_name, _) in zip(results, test_incr_list):
    print(f"{test_name}: {result}")
```