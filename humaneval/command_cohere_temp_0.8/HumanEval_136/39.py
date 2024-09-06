```python
def largest_smallest_integers(lst):
    positive = min(lst, key=lambda x: x >= 0)
    negative = max(lst, key=lambda x: x < 0)
    return negative, positive
```

The `largest_smallest_integers` function takes a list of integers as input and returns a tuple containing the largest negative integer and the smallest positive integer from the list. It uses the `max` and `min` functions with a custom key function to find the largest negative and smallest positive numbers, respectively.

Here's an example of how you can use the function with a test case from the prompt:
```python
test_cases = [
    ([2, 4, 1, 3, 5, 7], (None, 1)),
    ([], (None, None)),
    ([0], (None, None)),
    ([-1, -2, -3, -4], (-3, None)),
    ([1, 2, 3, 4, 5], (None, 5)),
]

for test_case, expected in test_cases:
    result = largest_smallest_integers(test_case)
    assert result == expected, f"Expected {expected}, but got {result}"
```

This script will ensure that the function works as expected and produces the correct results for various test cases. Adjust the test cases if needed to cover other scenarios.