Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set, which corresponds to the number of distinct characters in the string, regardless of case.

To test this function, you can use the following code:
```python
test_cases = [
    ('xyzXYZ', 3),
    ('Jerry', 4),
    (# Tests with Unicode characters
    ('𝄞yz𝄞XYZ', 3),
    ('𝔾𝕦𝕤𝕡𝕘𝕕', 5)
    # More tests can be added as needed...
])

for arg, expected in test_cases:
    assert count_distinct_characters(arg) == expected, f"For input:{arg}, the expected result is {expected}, but the actual result is {count_distinct_characters(arg)}."
```
The tests provided cover both ASCII and Unicode characters to ensure the function's correctness across different character sets.