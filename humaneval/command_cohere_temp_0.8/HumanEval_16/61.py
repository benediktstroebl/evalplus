Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(s: str) -> int:
    return len(set(s.lower()))
```
This function uses a set to calculate the distinct characters in the provided string, irrespective of case, and then returns the count of those distinct characters.

To test this function, you can execute the following commands:
```python
test_cases = [
    ('xyzXYZ', 3),
    ('Jerry', 4),
    (# Test with an empty string
    '', 0),
    (# Test with a string having only one unique character
    'ffa', 1),
    (# Test with a string having multiple repetitions of the same character
    'bbbb', 1),
]

for string, expected in test_cases:
    observed = count_distinct_characters(string)
    assert observed == expected, f"For '{string}', expected {expected} distinct characters but found {observed}"
```
This block of code helps verify the functionality of the `count_distinct_characters` function against multiple scenarios.