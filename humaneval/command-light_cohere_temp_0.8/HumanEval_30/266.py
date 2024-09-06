```python
def get_positive(l: list):
    """Return only positive numbers in the list"""
    return [num for num in l if num > 0]

# Test cases
test_get_positive = []
test_cases = [
    [-1, 2, -4, 5, 6],
    [5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10],
])

# Loop through test cases and assert result
for test_case in test_cases:
    assert get_positive(test_case) == [2, 5, 6, 3, 9, 123, 1], "Passed test case: " + str(test_case) + \"!\\"
```
This code defines a function **get_positive** that returns a list of positive numbers from the input list, and provides test cases to ensure that the function is working correctly. The script also includes an descriptive string that will be shown when the script is run, to better explain what the code does.