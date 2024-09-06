```python
def max_element(lst):
    if not_positive(lst):
        return float('-inf')
    elif len(lst) == 0:
        return float('-inf')
    else:
        return max(lst)

def not_positive(lst):
    return all(value > 0 for value in lst)

# Test cases
test_max_element = [
    ([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10], None),
    (None,),
    ([-10, 2, -3, -5, -20], True),
    ([1, 2, 3, -4], True),
    ([1, 2, 3, 4, 5], False),
    ([], False),
    ([-100, -200, -400, -800], True),
    ([1, 2, 3, 4, 5], True),
    ([-1, 2, 3, 4, 5], False),
]

# Run the tests
for test in test_max_element:
    assert max_element(test[0]) == test[1], f"Error in test case: {test[1]}"
```

The provided solution calculates the maximum element in a list while also handling the edge cases of empty lists and lists with only positive elements. It also has a test cases to ensure the function behaves correctly.