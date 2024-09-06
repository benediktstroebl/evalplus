```python
def count_distinct_characters(string: str):
    return len({c for c in string.org.lower() if c not in string})

# Unit tests
test_distinct_characters = TestDistinctCharacters()
test_distinct_characters.test()

def TestDistinctCharacters():
    assert count_distinct_characters("xyzXYZ") == 3
    assert count_distinct_characters("Jerry") == 4
```