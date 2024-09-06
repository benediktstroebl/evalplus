Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to remove duplicate characters and converts the input string to lowercase to ensure that characters are case-insensitive. Case-insensitive character counting is a crucial requirement as mentioned in the problem statement.

The function returns the number of distinct characters in the set, which corresponds to the number of distinct characters in the input string.

The tests for this function can be run using the following code:
```python
test_cases = [
    ("xyzXYZ", 3),
    ("Jerry", 4),
    (" cooperated", 6),
    ("alphaBeta", 6),
    ("Let's Gulp!', 8),
]

for inp, out in test_cases:
    assert count_distinct_characters(inp) == out, f"For input: {inp}, expected: {out}, got: {count_distinct_characters(inp)}"
```