```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.string() if c.isalpha() and.

def test_count_distinct_characters(string: str) -> None:
    try:
        result = count_distinct_characters(string)
        assert result == len({c for c in string if c.isalpha()})
       
    assert len({c for c in string if c.isalpha()}) == result
        done()
``` 
The function `count_distinct_characters` calculates the count of unique characters in a given string. The function `test_count_distinct_characters` is a test case that verifies if the `count_distinct_characters` function is working correctly.