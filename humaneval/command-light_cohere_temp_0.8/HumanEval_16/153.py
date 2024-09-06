```python
def count_distinct_characters(string):
    """ Returns the count of distinct characters in the string (case-insensitive) """
    string = string.upper()  #
    specific_characters only once, regardless of case.")
    char_count = set()
    for c in string:
        char_count.add(c.isupper())
    unique
    particular character of the time.")
    return len(char_count)

# Unit tests
test_count_distinct_characters = """
def test_count_distinct_characters():
    assert count_distinct_characters('XYZ') == 3  # Should be 3
 assert count_distinct_characters('jerry') == 4  # Should be 4
assert count_distinct_characters('  junk') == 4  # Should be 4
 assert count_distinct_characters('ABC123') == 5  # Should be 5
 pass
test_count_distinct_characters()
```