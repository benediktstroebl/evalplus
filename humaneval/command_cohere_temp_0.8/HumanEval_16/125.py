Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the given string, regardless of case, and then returns the set's length to provide the number of distinct characters.

Here's how you can use it and provide tests:
```python
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('Hello, World!') == 7
    assert count_distinct_characters('...') == 3

test_count_distinct_characters()
```
This will provide a test suite with four tests, and the code is self-contained within the `count_distinct_characters` function.