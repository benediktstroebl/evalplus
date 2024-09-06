```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num >= 0]

#Test cases
test_get_positive = []
test_cases = [
    [],  # Empty list
    [-1, 2, -4, 5, 6],  # Negatives
    5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],  # Mixed values and positives
]

# Loop through test cases
for test_case in test_cases:
    actual_list = [x for x in test_case]
    assert get_positive(actual_list) == [x for x in test_case if x >= 0],\
        f"Failed in test case: {test_case}\n"
    test_get_positive.

# Example
print("Test cases passed!")
```