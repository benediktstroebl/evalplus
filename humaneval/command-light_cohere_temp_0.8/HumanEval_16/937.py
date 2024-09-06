```python
def count_distinct_characters(string: str):
    """ Returns the number of distinct characters in the string (case-insensitive)"""
    # converts string to lowercase and remove all non-alph characters
    char_set = set(string.lower().filter(str.notalpha()))
   ows arereturn distinct characters
    return len(char_set)

# tests
def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3  # Should return 3
    assert count_distinct_characters('jerry') == 4  # Should return 4

test_distinct_characters()
```