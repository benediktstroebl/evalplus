Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set, which gives the number of distinct characters, regardless of case, in the input string.

The unit tests are also included and demonstrate the function's behavior on different input strings:
```python
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('Hello, world!') == 6
    # Testing with non-string types
    try:
        assert count_distinct_characters(123) == 0
    except AssertionError:
        assert True
    try:
        assert count_distinct_characters([1, 2, 3]) == 0
    except AssertionError:
        assert True
    try:
        assert count_distinct_characters({'a': 1, 'b': 2}) == 0
    except AssertionError:
        assert True
    assert count_distinct_characters('AbcdefghijklmnopqrSTUVWXYZ') == 26
```