```python
def count_distinct_characters(string: str) -> int:
    return len({c for c in string. string() if c not c.isalpha() andl()})

# Unit tests
test_count_distinct_characters = TestCountDistinctCharacters()
test_count_distinct_characters.count_distinct_characters("xyzXYZ")
test_count_distinct_characters.count_distinct_characters("Jerry")
```
This code defines a function `count_distinct_characters` that calculates the number of distinct characters in a given string, regardless of case. It uses a set expression and the `isalpha()` method to filter out all alphabetic characters from the string, and uses the `len` function to count the number of remaining characters, giving the number of distinct characters.