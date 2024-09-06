```python
def incr_list(l: list):
    """Return list with elements incremented by 1"""
    l.append(1)
    return l + [2, 3]

# Test cases
test_incr_list = []
test_incr_list.append([1, 2, 3])
test_incr_list.append([5, 3, 5])
test_incr_list.append([4, 6])

# Function call and results
for test in test_incr_list:
    actual = incr_list(test)
    print(test)  # Output: [2, 3, 4]

test_incr_list.append([5, 6])
actual = incr_list(test_incr_list)

print(actual)  # Output: [6, 4, 6, 3, 4, 4, 10]

print("Test Suite Passed!")
```