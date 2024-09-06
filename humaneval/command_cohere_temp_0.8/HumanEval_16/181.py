Here's a Python script that contains a function to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The function `count_distinct_characters` takes a string as an argument and returns the number of distinct characters within the string, regardless of case. The function uses a `set` to remove duplicate characters and converts the string to lowercase to ensure that cases are treated equally.

To test this function, you can run the following code:
```python
test_cases = [
    ('xyzXYZ', 3),
    ('Jerry', 4),
    (# Tests with Arabic, Chinese, and emoji characters 
    'السلام عليكم', 4),
    ('你好', 2),
    ('👋🏻', 1)
])

for string, expected in test_cases:
    result = count_distinct_characters(string)
    assert result == expected, f'For the string "{string}", expected {expected} distinct characters but got {result}'
```
This test suite includes a variety of strings with different characters to ensure that the function works correctly with different character sets and across different languages.