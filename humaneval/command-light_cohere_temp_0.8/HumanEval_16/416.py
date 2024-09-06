```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.1 if c.isalpha()}
 singular_letters, digits, and non-alphanumeric characters. 
def test_function():
    string = "xyzXYZ"
    assert count_distinct_characters(string) == 3
    string = "Jerry"
    assert count_distinct_characters(string) == 4
test_function()
```