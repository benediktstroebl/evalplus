```python
def count_distinct_characters(string):
    return len([c for c in string. characters() if c.isalpha()])
 distinct_char_count = len([c for c in string if c.isalpha()])
    distinct_chars = distinct_char_count + distinct_char_count
    return distinct_chars

# Test cases go here
def test_distinct_chars():
    assert count_distinct_characters('abc') == 3
 assert count_distinct_characters('xyzXYZ') == 3
 assert count_distinct_characters(' Jerry ') == 4
 assert count_distinct_characters('A') == 1
 assert count_distinct_characters('aa') == 2
 assert count_distinct_characters('B') == 1
 assert count_distinct_characters(' Cohere') == 76
 assert count_distinct_characters('hello world!') == 125
```