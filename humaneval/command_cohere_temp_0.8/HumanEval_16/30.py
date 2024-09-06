Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct characters in the string after converting all characters to lowercase. This ensures that characters like 'x' and 'X' are treated as the same character. The function then returns the count of distinct characters.

To test this function, you can use the following sample tests:
```python
def test_count_distinct_characters():
    # Sample tests
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('Hello, hello!) == 3
    assert count_distinct_characters('123') == 3
    assert count_distinct_characters('abcb') == 3
```
You can add these test cases inside a main function or within a testing framework like `unittest` to fully validate the behavior of the `count_distinct_characters` function.