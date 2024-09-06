Here's the Python code with a self-contained function `count_distinct_characters` that solves the problem:
```python
def count_distinct_characters(string: str) -> int:
    characters = set(string.lower())
    return len(characters)
```
This function uses a set to store the distinct lowercase characters only once, and then calculates the length of this set, which gives the number of distinct characters. The function ignores the case, counting 'X' and 'x' as the same character. 

Here is how you can use this function in a unit test:
```python
def test_count_distinct_characters():
    # Test case one
    assert count_distinct_characters('xyzXYZ') == 3

    # Test case two
    assert count_distinct_characters('Jerry') == 4
``` 
This test verifies that the function behaves as expected, in line with the problem's description.