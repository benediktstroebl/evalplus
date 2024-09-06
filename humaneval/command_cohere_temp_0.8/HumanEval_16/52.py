Here's a Python script with a self-contained function that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
The function lowercases the input string to ensure case insensitivity, converts it to a set to remove duplicate characters, and then gets the size of the resulting set which is the number of distinct characters.

To apply this function to test cases, the script should include a test block like this:
```python
def test_count_distinct_characters():
    # Test case 1
    assert count_distinct_characters('xyzXYZ') == 3

    # Test case 2
    assert count_distinct_characters('Jerry') == 4

test_count_distinct_characters()
```
The total line `test_count_distinct_characters()` executes the function test_count_distinct_characters which incorporates the test block and asserts the function `count_distinct_characters` behaves accordingly. 
If the function behaves correctly, the test block will output `OK`.