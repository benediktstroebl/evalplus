Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are treated as the same character. The function then returns the count of distinct characters.

To test this function, you can use the following code:
```python
test_cases = [
    ('xyzXYZ', 3),
    ('Jerry', 4),
    (# Test with an empty string
     '', 0),
    (# Test with a string with a number
     '12334', 1),
    (# Test with a string with multiple numbers
     '123AAA456', 3),
]

for input, expected in test_cases:
    assert count_distinct_characters(input) == expected
```
This block of code provides test cases that cover different scenarios and ensures that the function `count_distinct_characters` behaves as expected.