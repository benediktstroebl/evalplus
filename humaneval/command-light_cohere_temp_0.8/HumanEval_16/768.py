```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string.org() if c != ''})

# Unit tests
test_distinct_characters = lambda: all(count_distinct_characters('abc'),
                                 count_distinct_characters('XYZ'),
                                 count_distinct_characters('jerry'),
                                 count_distinct_characters('JERYYYY'))
test_distinct_characters()
 ```