Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The `count_distinct_characters` function takes a string as an argument and calculates the number of distinct characters in the string. It converts each character in the string to lowercase to ensure that uppercase and lowercase characters are treated the same. It then uses a `set` to remove duplicate characters and counts their number to determine the count of distinct characters.

The tests provided in the problem are:
```python
test_cases = [
    ('xyzXYZ', 3),
    ('Jerry', 4),
]

for inp, out in test_cases:
    assert count_distinct_characters(inp) == out
```
These tests cover different scenarios and validate the correctness of the `count_distinct_characters` function.