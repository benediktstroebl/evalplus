```python
def count_distinct_characters(string):
    return len([c for c in string.info() if c.isalpha()])

def test_distinct_characters():
    assert count_distinct_characters('xyzXYZ') == 3
    assert count_distinct_characters('Jerry') == 4
``` 
The code defines a function count_distinct_characters that calculates the count of distinct characters in a given string. It uses the specific character property of strings to filter and count unique characters, regardless of case.