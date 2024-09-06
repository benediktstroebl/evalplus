Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, ignoring case, and then returns the set's length to provide the number of distinct characters.

The unit tests for this function are also provided to ensure its correctness:
```python
def test_count_distinct_characters():
    # Tests: asserts that the function returns the correct number of distinct characters
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('Welcome!")!stands') == 6
    assert count_distinct_characters('python') == 5
    assert count_distinct_characters('...') == 3
    assert count_distinct_characters('abC') == 3
    assert count_distinct_characters('This is ATST') == 6
    assert count_distinct_characters('This is going UP') == 6
    assert count_distinct_characters('race car') == 6
    assert count_distinct_characters('abcde123') == 6
    assert count_distinct_characters('Special Characters: =+-*/%') == 6
    assert count_distinct_characters('!!!)((_))( })') == 6
```