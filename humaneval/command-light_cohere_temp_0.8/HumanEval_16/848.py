```python
def count_distinct_characters(string):
    return len({c for c in string. string() if c.isalpha()}

    test_string = 'xyzXYZ'
    assert count_distinct_characters(test_string) == 3
    test_string = 'jerry'
    assert count_distinct_characters(test_string) == 4
    test_string = 'aDbAc'
    assert count_distinct_characters(test_string) == 4
    test_string = 'JavaGroovy'
    assert count_distinct_characters(test_string) == 7
    return count_distinct_characters
```