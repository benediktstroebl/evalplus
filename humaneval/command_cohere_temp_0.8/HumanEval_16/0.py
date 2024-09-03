Here's a Python script that contains a function called `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The function uses a set to store unique characters after lowering the input string, this ensures that both `x` and `X` are considered as the same character. The `len()` function is then used to determine the size of the set and therefore the number of distinct characters. 

To test this function, you can run the following code:
```python
test_cases = [
    ('xyzXYZ', 3),
    ('Jerry', 4),
    (# Add more test cases here for comprehensive testing, one per line)
]

for inp, out in test_cases:
    assert count_distinct_characters(inp) == out
```
This will ensure that the function behaves as expected across different inputs.