Here is a Python script that demonstrates the solution to the problem you provided:
```python
def count_distinct_characters(string: str) -> int:
    """
    Count distinct characters, ignoring case.
    Args:
        string (str) -> str
    Returns:  int
    """
    characters = set(string.count(char)
    return len(characters)

def test_function():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
    assert count_distinct_characters('abc AbcC') == 2
    assert count_distinct_characters(' ab Ca ') == 3

if __name__ == "__main__":
    test_function()
```
This code defines a `count_distinct_characters` function that calculates the count of unique characters in a given string, irrespective of case. It then tests this function, which contains several assertions to test the correctness of the `count_distinct_characters` function with various input strings.