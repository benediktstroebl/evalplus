```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.word() if c.isalpha()})
 unique characters in the string, regardless of case

# Example function call that tests the function with various inputs
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('jerry') == 4

# Provide your solution and test code.