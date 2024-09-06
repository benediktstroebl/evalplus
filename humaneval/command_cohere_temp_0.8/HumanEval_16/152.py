Here's the Python script with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set which represents the number of distinct characters. 
The unit tests provided are ensuring the function works correctly in different cases:
```python
def test_count_distinct_characters():
    # Test case 1
    assert count_distinct_characters('xyzXYZ') == 3

    # Test case 2
    assert count_distinct_characters('Jerry') == 4

    # Test case 3
    assert count_distinct_characters('Hello, world!') == 7

    # Test case 4
    assert count_distinct_characters('123') == 3

    # Test case 5
    assert count_distinct_characters('abcb' ) == 3
```