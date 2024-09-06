Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are considered the same. The function then returns the count of distinct characters.

To test this function, you can run the following code:
```python
test_cases = [
    ('xyzXYZ', 3),
    ('Jerry', 4),
    (# Test with an empty string
    '', 0),
    (# Test with a string having only one character
    'ee', 1),
    (# Test with a string having digits and alphabets
    'a1b2c3', 3),
    (# Test with diacritics
    'éàö', 3)
]

for input, expected in test_cases:
    result = count_distinct_characters(input)
    assert result == expected
```
This script provides a function that solves the problem and includes test cases to validate its correctness.