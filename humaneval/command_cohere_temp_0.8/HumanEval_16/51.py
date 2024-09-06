Here's the Python code to solve the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters_set = set(string.lower())
    return len(characters_set)
```
The function `count_distinct_characters` takes a string as an argument and returns the number of distinct characters, case-insensitive, in the string. It uses a set to remove duplicate characters and lowercases all characters before counting.

Here's a test suite to test the function:
```python
def test_count_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('Hello, world!') == 6
    # Testing with non-alphabetic characters
    assert count_distinct_characters('123abc') == 3
    assert count_distinct_characters('3ae243r6') == 3
    assert count_distinct_characters('$@tyuman') == 4    
``` 
The test suite covers different scenarios to make sure the `count_distinct_characters` function works correctly.